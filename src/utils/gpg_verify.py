from pathlib import Path
import subprocess
import tempfile


class GPGVerifier:
    def __init__(self, public_key: Path) -> None:
        self.public_key = public_key

    def verify(self, signature_file: Path, data_file: Path) -> None:
        if not self.public_key.exists():
            raise FileNotFoundError(f"Public key not found: {self.public_key}")

        if not signature_file.exists():
            raise FileNotFoundError(f"Signature file not found: {signature_file}")

        if not data_file.exists():
            raise FileNotFoundError(f"Data file not found: {data_file}")

        with tempfile.TemporaryDirectory() as gnupg_home:
            self._import_key(Path(gnupg_home))
            self._verify_signature(Path(gnupg_home), signature_file, data_file)

    def _import_key(self, gnupg_home: Path) -> None:
        result = subprocess.run(
            [
                "gpg",
                "--homedir", str(gnupg_home),
                "--batch",
                "--import",
                str(self.public_key),
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(
                "GPG key import failed:\n"
                f"STDOUT:\n{result.stdout}\n"
                f"STDERR:\n{result.stderr}"
            )

    def _verify_signature(
        self,
        gnupg_home: Path,
        signature_file: Path,
        data_file: Path,
    ) -> None:
        result = subprocess.run(
            [
                "gpg",
                "--homedir", str(gnupg_home),
                "--batch",
                "--verify",
                str(signature_file),
                str(data_file),
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(
                "GPG verification failed:\n"
                f"STDOUT:\n{result.stdout}\n"
                f"STDERR:\n{result.stderr}"
            )