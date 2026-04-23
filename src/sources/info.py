from config.models import Config


class DebianIsoInfoBuilder:
    BASE_URL = "https://cdimage.debian.org/cdimage/archive"

    def __init__(self, config: Config) -> None:
        self.version = config.iso.version
        self.arch = config.iso.arch

    def info(self) -> dict:
        base_url = f"{self.BASE_URL}/{self.version}/{self.arch}/iso-cd"
        iso_name = f"debian-{self.version}-{self.arch}-netinst.iso"

        return {
            "version": self.version,
            "arch": self.arch,
            "base_url": base_url,
            "iso_name": iso_name,
            "iso_url": f"{base_url}/{iso_name}",
            "sha256_url": f"{base_url}/SHA256SUMS",
            "sha256_sign_url": f"{base_url}/SHA256SUMS.sign",
        }