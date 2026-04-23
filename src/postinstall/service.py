from pathlib import Path

from config.models import Config
from config.paths import POSTINSTALL_SCRIPT_PATH, TEMPLATES_DIR
from postinstall.builder import PostinstallBuilder
from postinstall.renderer import PostinstallRenderer


class PostinstallService:
    AUTHORIZED_KEYS_TEMPLATE = "postinstall/10_inject_authorized_keys.sh.j2"

    def __init__(self) -> None:
        self.renderer = PostinstallRenderer(TEMPLATES_DIR)

    def run(self, config: Config, build_dir: Path) -> dict:
        builder = PostinstallBuilder(build_dir)

        context = config.model_dump()

        rendered_script = self.renderer.render(
            self.AUTHORIZED_KEYS_TEMPLATE,
            context,
        )

        authorized_keys_script_path = builder.build_authorized_keys_script(
            rendered_script
        )

        # 🔥 ahora usamos path centralizado
        post_install_script_path = builder.copy_post_install_script(
            POSTINSTALL_SCRIPT_PATH
        )

        public_key_path = builder.copy_public_key(config.openssh.public_key_path)

        return {
            "authorized_keys_script": authorized_keys_script_path,
            "post_install_script": post_install_script_path,
            "public_key": public_key_path,
        }