import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from flask_frozen import Freezer
from jinja2 import FileSystemLoader, Environment, select_autoescape

from app import app


def _freeze_site(base_path: Path) -> None:
    """Freeze Flask site to static files."""
    app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True
    app.config["FREEZER_DESTINATION"] = str(base_path.resolve())
    freezer = Freezer(app)
    freezer.freeze()


def _fix_pages(base_path: Path) -> None:
    """For bare files, replace with a directory containing an index.html file."""
    files = [p for p in base_path.rglob("*") if p.is_file()]
    files.sort(key=lambda p: len(p.relative_to(base_path).parts), reverse=True)

    for path in files:
        # Skip if path no longer exists or has become a directory
        if not path.exists() or path.is_dir():
            continue

        relative = path.relative_to(base_path)
        if relative.name == "index.html":
            continue

        new_dir = base_path / relative.parent / relative.stem

        # If a file exists where we need a directory, move it to `_`,
        # create the directory, then move `_` to `index.html`.
        if new_dir.exists() and new_dir.is_file():
            underscore = new_dir.with_name("_")
            new_dir.replace(underscore)
            new_dir.mkdir(parents=True, exist_ok=True)
            underscore.replace(new_dir / "index.html")
            continue  # Already moved, skip the regular move below

        new_dir.mkdir(parents=True, exist_ok=True)
        path.replace(new_dir / "index.html")


def _build_styles(base_path: Path) -> None:
    """
    Generate Tailwind CSS styles.

    Based on Lantern v0.5.0 build process.
    """
    tw_bin = Path(".venv/bin/tailwindcss")
    styles_path = Path(__file__).parent / "styles"
    output_path = base_path / "static" / "css" / "main.css"

    _jinja = Environment(
        loader=FileSystemLoader(styles_path), autoescape=select_autoescape()
    )
    src_css = _jinja.get_template("main.css.j2").render(site_path=base_path.resolve())
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as tmp_dir:
        src_path = Path(tmp_dir) / "main.src.css"
        with src_path.open("w") as src_file:
            src_file.write(src_css)

        subprocess.run(  # noqa: S603
            [
                tw_bin,
                "-i",
                str(src_path.resolve()),
                "-o",
                str(output_path.resolve()),
                "--minify",
            ],
            check=True,
        )

    # append trailing new line
    with output_path.open("a") as out_file:
        out_file.write("\n")


def _copy_static(base_path: Path) -> None:
    types = ["fonts", "img", "txt"]
    for t in types:
        static_path = Path(__file__).parent / t
        output_path = base_path / "static" / t
        shutil.copytree(static_path, output_path)


def main() -> None:
    """Entrypoint."""
    output_path = Path(__file__).parent.parent / "build"

    if output_path.exists():
        shutil.rmtree(output_path)

    _freeze_site(output_path)
    _fix_pages(output_path)
    _copy_static(output_path)
    _build_styles(output_path)


if __name__ == "__main__":
    main()
