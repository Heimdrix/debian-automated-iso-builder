from pathlib import Path
import shutil
import subprocess


class IsoExtractor:
    def extract(self, iso_path: Path, output_dir: Path) -> Path:
        if not iso_path.exists():
            raise FileNotFoundError(f"ISO not found: {iso_path}")

        if output_dir.exists():
            shutil.rmtree(output_dir)

        output_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            "xorriso",
            "-osirrox", "on",
            "-indev", str(iso_path),
            "-extract", "/",
            str(output_dir),
        ]

        subprocess.run(cmd, check=True)
        self._make_writable(output_dir)

        return output_dir

    def _make_writable(self, directory: Path) -> None:
        subprocess.run(
            ["chmod", "-R", "u+w", str(directory)],
            check=True,
        )