from pathlib import Path
import subprocess


class IsoMetadata:
    def get_volume_id(self, iso_path: Path) -> str:
        cmd = [
            "xorriso",
            "-indev",
            str(iso_path),
            "-pvd_info",
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )

        output = result.stdout + "\n" + result.stderr

        for line in output.splitlines():
            if "Volume id" in line or "Volume Id" in line or "Volume" in line:
                if ":" in line:
                    return line.split(":", 1)[1].strip().strip("'")

        raise RuntimeError("Volume ID not found in ISO")