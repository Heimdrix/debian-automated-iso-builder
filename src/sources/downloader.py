from config.paths import CACHE_ISO_DIR
from utils.downloader import download_file

import shutil


class IsoDownloader:
    def download(self, iso: dict) -> dict:
        iso_url = iso["iso_url"]
        sha256_url = iso["sha256_url"]
        sha256_sign_url = iso["sha256_sign_url"]

        iso_name = iso["iso_name"]
        iso_dir = CACHE_ISO_DIR / iso_name.removesuffix(".iso")

        iso_dir.mkdir(parents=True, exist_ok=True)

        iso_path = iso_dir / iso_name
        sha256_path = iso_dir / "SHA256SUMS"
        sha256_sign_path = iso_dir / "SHA256SUMS.sign"

        try:
            download_file(iso_url, iso_path)
            download_file(sha256_url, sha256_path)
            download_file(sha256_sign_url, sha256_sign_path)

            return {
                "iso_dir": iso_dir,
                "iso": iso_path,
                "sha256": sha256_path,
                "sha256_sign": sha256_sign_path,
            }

        except Exception:
            if iso_dir.exists():
                shutil.rmtree(iso_dir)
            raise