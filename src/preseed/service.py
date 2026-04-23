from pathlib import Path

from config.models import Config
from config.paths import TEMPLATES_DIR
from preseed.renderer import PreseedRenderer
from preseed.builder import PreseedBuilder


class PreseedService:
    TEMPLATE_NAME = "preseed/preseed.cfg.j2"

    def __init__(self) -> None:
        self.renderer = PreseedRenderer(TEMPLATES_DIR)

    def run(self, config: Config, build_dir: Path) -> Path:
        builder = PreseedBuilder(build_dir)

        context = config.model_dump()
        context["recipe"] = config.preseed.recipe_path.stem

        rendered_preseed = self.renderer.render(
            self.TEMPLATE_NAME,
            context,
        )

        builder.copy_recipe(config.preseed.recipe_path)
        output_path = builder.build_preseed(rendered_preseed)

        return output_path