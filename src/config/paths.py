from pathlib import Path


# --- Base ---
BASE_DIR = Path(__file__).resolve().parents[2]

# --- Assets ---
ASSETS_DIR = BASE_DIR / "assets"
GRUB_CONFIG_PATH = ASSETS_DIR / "boot" / "grub" / "grub.cfg"
POSTINSTALL_SCRIPT_PATH = ASSETS_DIR / "preseed" / "postinstall" / "post_install.sh"

# --- Cache ---
CACHE_DIR = BASE_DIR / "cache"
CACHE_BUILD_DIR = CACHE_DIR / "build"
CACHE_ISO_DIR = CACHE_DIR / "iso"
CACHE_WORK_DIR = CACHE_DIR / "work"

# --- Config ---
CONFIG_DIR = BASE_DIR / "config"
DEFAULT_CONFIG_PATH = CONFIG_DIR / "default.yml"
PROFILES_DIR = CONFIG_DIR / "profiles"

# --- Keys ---
KEYS_DIR = BASE_DIR / "keys"
DEBIAN_PUBLIC_KEY_PATH = KEYS_DIR / "debian" / "debian-cd-signing-key.asc"

# --- Output ---
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_ISO_DIR = OUTPUT_DIR / "iso"

# --- Templates ---
TEMPLATES_DIR = BASE_DIR / "templates"