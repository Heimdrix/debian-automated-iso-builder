from datetime import datetime


def build_dir_name(hostname: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{hostname}-build-{timestamp}"