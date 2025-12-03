from pathlib import Path

from flask_frozen import Freezer

from app import app

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


output_path = Path(__file__).parent.parent / "build"

app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_DESTINATION'] = str(output_path.resolve())
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    _fix_pages(output_path)
