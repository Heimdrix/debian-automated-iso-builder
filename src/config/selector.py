from pathlib import Path

from config.paths import PROFILES_DIR, DEFAULT_CONFIG_PATH


class ConfigSelector:
    def select(
        self,
        profile: str | None = None,
        config_path: str | None = None,
    ) -> Path:
        if profile and config_path:
            raise ValueError("Use either 'profile' or 'config_path', not both")

        if config_path:
            path = Path(config_path)
        elif profile:
            path = PROFILES_DIR / f"{profile}.yml"
        else:
            path = DEFAULT_CONFIG_PATH

        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        return path