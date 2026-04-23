import logging

from dotenv import load_dotenv

from config.selector import ConfigSelector
from config.loader import ConfigLoader
from config.validator import validate_config
from pipeline.orchestrator import run_pipeline


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    load_dotenv()

    selector = ConfigSelector()
    config_path = selector.select()

    loader = ConfigLoader()
    config_data = loader.load(config_path)

    config = validate_config(config_data)

    logging.info("Config loaded successfully")
    logging.info("Hostname: %s", config.network.hostname)

    run_pipeline(config)


if __name__ == "__main__":
    main()