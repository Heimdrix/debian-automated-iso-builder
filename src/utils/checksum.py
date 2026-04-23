from pathlib import Path
import hashlib


class ChecksumVerifier:
    def __init__(self, checksum_file: Path) -> None:
        self.checksum_file = checksum_file

    def verify(self, file_path: Path) -> None:
        expected_checksum = self._get_expected_checksum(file_path.name)
        actual_checksum = self._calculate_sha256(file_path)

        if expected_checksum != actual_checksum:
            raise ValueError(
                f"Checksum mismatch for {file_path.name}: "
                f"expected {expected_checksum}, got {actual_checksum}"
            )

    def _calculate_sha256(self, file_path: Path) -> str:
        sha256_hash = hashlib.sha256()

        with file_path.open("rb") as file_handle:
            for chunk in iter(lambda: file_handle.read(8192), b""):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    def _get_expected_checksum(self, filename: str) -> str:
        with self.checksum_file.open("r", encoding="utf-8") as file_handle:
            for line in file_handle:
                parts = line.strip().split(maxsplit=1)

                if len(parts) != 2:
                    continue

                expected_checksum, listed_filename = parts

                listed_filename = listed_filename.removeprefix("*")
                listed_filename = listed_filename.removeprefix("./")

                if listed_filename == filename:
                    return expected_checksum

        raise ValueError(f"Checksum not found for {filename}")