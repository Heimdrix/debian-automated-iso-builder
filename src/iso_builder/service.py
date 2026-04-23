from pathlib import Path
from datetime import datetime
import shutil

from config.models import Config
from config.paths import CACHE_WORK_DIR, GRUB_CONFIG_PATH, OUTPUT_ISO_DIR

from iso_builder.extractor import IsoExtractor
from iso_builder.injector import IsoInjector
from iso_builder.metadata import IsoMetadata
from iso_builder.builder import IsoBuilder


class IsoBuilderService:
    def __init__(self) -> None:
        self.extractor = IsoExtractor()
        self.injector = IsoInjector()
        self.metadata = IsoMetadata()
        self.builder = IsoBuilder()

    def run(self, config: Config, build_dir: Path, downloaded_files: dict) -> Path:
        iso_path = downloaded_files["iso"]

        work_dir = CACHE_WORK_DIR / build_dir.name
        iso_work_dir = work_dir / "iso"

        if work_dir.exists():
            shutil.rmtree(work_dir)

        work_dir.mkdir(parents=True, exist_ok=True)

        try:
            extracted_iso_dir = self.extractor.extract(iso_path, iso_work_dir)

            self.injector.inject_preseed(build_dir, extracted_iso_dir)
            self.injector.inject_grub(GRUB_CONFIG_PATH, extracted_iso_dir)
            self.injector.regenerate_md5(extracted_iso_dir)

            volume_id = self.metadata.get_volume_id(iso_path)

            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            output_iso_path = (
                OUTPUT_ISO_DIR
                / f"{config.network.hostname}-debian-{config.iso.version}-{config.iso.arch}-{timestamp}.iso"
            )

            return self.builder.build(extracted_iso_dir, output_iso_path, volume_id)

        finally:
            if work_dir.exists():
                shutil.rmtree(work_dir)