import logging

from config.models import Config
from config.paths import CACHE_BUILD_DIR

from pipeline.utils import build_dir_name

from sources.info import DebianIsoInfoBuilder
from sources.downloader import IsoDownloader
from sources.verifier import IsoVerifier

from preseed.service import PreseedService
from postinstall.service import PostinstallService
from iso_builder.service import IsoBuilderService


LOGGER = logging.getLogger(__name__)


def run_pipeline(config: Config) -> None:
    LOGGER.info("Starting pipeline...")

    build_name = build_dir_name(config.network.hostname)
    build_dir = CACHE_BUILD_DIR / build_name
    build_dir.mkdir(parents=True, exist_ok=True)

    LOGGER.info("Build directory: %s", build_dir)

    LOGGER.info("Step 1: Build source info")
    iso_info = DebianIsoInfoBuilder(config).info()

    LOGGER.info("Step 2: Download source files")
    downloaded_files = IsoDownloader().download(iso_info)
    LOGGER.info("ISO downloaded: %s", downloaded_files["iso"])

    LOGGER.info("Step 3: Verify source files")
    IsoVerifier().verify(downloaded_files)
    LOGGER.info("Source files verified")

    LOGGER.info("Step 4: Generate preseed")
    preseed_output_path = PreseedService().run(config, build_dir)
    LOGGER.info("Preseed generated: %s", preseed_output_path)

    LOGGER.info("Step 5: Generate postinstall")
    postinstall_output = PostinstallService().run(config, build_dir)
    LOGGER.info("Postinstall script: %s", postinstall_output["post_install_script"])
    LOGGER.info(
        "Authorized keys script: %s",
        postinstall_output["authorized_keys_script"],
    )
    LOGGER.info("Public key copied: %s", postinstall_output["public_key"])

    LOGGER.info("Step 6: Build final ISO")
    final_iso_path = IsoBuilderService().run(config, build_dir, downloaded_files)
    LOGGER.info("Final ISO built: %s", final_iso_path)

    LOGGER.info("Pipeline completed successfully")