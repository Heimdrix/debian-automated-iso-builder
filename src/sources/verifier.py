from config.paths import DEBIAN_PUBLIC_KEY_PATH
from utils.checksum import ChecksumVerifier
from utils.gpg_verify import GPGVerifier


class IsoVerifier:
    def __init__(self) -> None:
        self.gpg_verifier = GPGVerifier(DEBIAN_PUBLIC_KEY_PATH)

    def verify(self, downloaded_files: dict) -> None:
        iso_path = downloaded_files["iso"]
        sha256_path = downloaded_files["sha256"]
        sha256_sign_path = downloaded_files["sha256_sign"]

        self.gpg_verifier.verify(sha256_sign_path, sha256_path)

        checksum_verifier = ChecksumVerifier(sha256_path)
        checksum_verifier.verify(iso_path)