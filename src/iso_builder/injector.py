from pathlib import Path
import shutil
import subprocess


class IsoInjector:
    def inject_preseed(self, build_dir: Path, iso_dir: Path) -> Path:
        """
        Copia toda la carpeta preseed (incluyendo postinstall) dentro de la ISO.
        """
        source = build_dir / "preseed"
        target = iso_dir / "preseed"

        if not source.exists():
            raise FileNotFoundError(f"Preseed directory not found: {source}")

        if target.exists():
            shutil.rmtree(target)

        shutil.copytree(source, target)

        return target

    def inject_grub(self, grub_file: Path, iso_dir: Path) -> Path:
        """
        Sobrescribe el grub.cfg de la ISO.
        """
        target = iso_dir / "boot" / "grub" / "grub.cfg"

        if not grub_file.exists():
            raise FileNotFoundError(f"Grub config not found: {grub_file}")

        shutil.copyfile(grub_file, target)

        return target

    def regenerate_md5(self, iso_dir: Path) -> Path:
        """
        Regenera md5sum.txt tras modificar la ISO.
        """
        md5_path = iso_dir / "md5sum.txt"

        subprocess.run(
            [
                "bash",
                "-c",
                "find . -type f ! -name md5sum.txt -print0 | xargs -0 md5sum > md5sum.txt",
            ],
            cwd=iso_dir,
            check=True,
        )

        return md5_path