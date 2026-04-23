from pathlib import Path

from utils.file_utils import write_file, copy_file


class PreseedBuilder:
    def __init__(self, build_dir: Path) -> None:
        self.preseed_dir = build_dir / "preseed"
        self.preseed_output_path = self.preseed_dir / "preseed.cfg"
        self.recipes_output_dir = self.preseed_dir / "recipes"

    def build_preseed(self, rendered_preseed: str) -> Path:
        write_file(rendered_preseed, self.preseed_output_path)
        return self.preseed_output_path

    def copy_recipe(self, recipe_path: Path) -> Path:
        destination = self.recipes_output_dir / recipe_path.name
        copy_file(recipe_path, destination)
        return destination