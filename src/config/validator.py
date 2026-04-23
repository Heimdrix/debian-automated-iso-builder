from config.models import Config

def validate_config(config_data: dict) -> Config:
    return Config(**config_data)