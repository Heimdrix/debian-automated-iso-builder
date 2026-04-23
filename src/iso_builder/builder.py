from pathlib import Path
import subprocess
import shutil


class IsoBuilder:
    def __init__(self) -> None:
        self.xorriso_path = shutil.which("xorriso")

        if self.xorriso_path is None:
            raise RuntimeError("xorriso not found")

    def build(self, iso_dir: Path, output_iso: Path, volume_id: str) -> Path:
        output_iso.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            self.xorriso_path,
            "-as", "mkisofs",
            "-r",
            "-V", volume_id,
            "-o", str(output_iso),
            "-J", "-joliet-long", "-cache-inodes",
            "-eltorito-alt-boot",
            "-e", "boot/grub/efi.img",
            "-no-emul-boot",
            "-isohybrid-gpt-basdat",
            "-isohybrid-apm-hfsplus",
            ".",
        ]

        subprocess.run(cmd, cwd=iso_dir, check=True)

        return output_iso