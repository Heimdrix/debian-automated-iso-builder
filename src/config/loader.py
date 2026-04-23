import yaml
from pathlib import Path
from utils.env import expand_env_vars


class ConfigLoader:
    def load(self, path: Path) -> dict:
        config_text = self._read_config_text(path)
        expanded_config_text = expand_env_vars(config_text)
        return self._parse_config_yaml(expanded_config_text)

    def _read_config_text(self, path: Path) -> str:
        config_text = path.read_text(encoding="utf-8")

        if not config_text.strip():
            raise ValueError(f"Config file is empty: {path}")

        return config_text

    def _parse_config_yaml(self, config_text: str) -> dict:
        config_data = yaml.safe_load(config_text)

        if config_data is None:
            raise ValueError("Config file is empty after parsing")

        if not isinstance(config_data, dict):
            raise TypeError("Config root must be a YAML mapping")

        return config_data