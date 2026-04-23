from pathlib import Path
import urllib.request


def download_file(url: str, destination: Path) -> Path:
    if destination.exists():
        return destination

    destination.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, destination)
    return destination
