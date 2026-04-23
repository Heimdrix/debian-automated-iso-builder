from pathlib import Path
import shutil


def write_file(content: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def copy_file(source: Path, destination: Path) -> Path:
    if not source.exists():
        raise FileNotFoundError(f"Source file not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

    return destination