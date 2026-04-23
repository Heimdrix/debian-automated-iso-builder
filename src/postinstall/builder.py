from pathlib import Path

from utils.file_utils import write_file, copy_file


class PostinstallBuilder:
    def __init__(self, build_dir: Path) -> None:
        self.postinstall_dir = build_dir / "preseed" / "postinstall"
        self.openssh_dir = self.postinstall_dir / "openssh"

        self.authorized_keys_script_path = (
            self.openssh_dir / "10_inject_authorized_keys.sh"
        )
        self.post_install_script_path = self.postinstall_dir / "post_install.sh"

    def build_authorized_keys_script(self, rendered_script: str) -> Path:
        write_file(rendered_script, self.authorized_keys_script_path)
        return self.authorized_keys_script_path

    def copy_post_install_script(self, source_path: Path) -> Path:
        copy_file(source_path, self.post_install_script_path)
        return self.post_install_script_path

    def copy_public_key(self, public_key_path: Path) -> Path:
        destination = self.openssh_dir / public_key_path.name
        copy_file(public_key_path, destination)
        return destination