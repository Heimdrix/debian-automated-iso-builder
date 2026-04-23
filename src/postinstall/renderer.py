from pathlib import Path

from rendering.jinja import TemplateRenderer


class PostinstallRenderer:
    def __init__(self, template_dir: Path) -> None:
        self.renderer = TemplateRenderer(template_dir)

    def render(self, template_name: str, context: dict) -> str:
        return self.renderer.render(template_name, context)