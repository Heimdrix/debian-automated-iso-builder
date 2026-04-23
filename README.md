# Custom Debian ISO Generator for Automated Deployment (UEFI Only)

This project provides a Python-based pipeline to generate customized Debian ISO images for automated deployment.

It uses Jinja templating and a modular architecture to dynamically build installation media with reproducible and secure configurations.

The primary use case is automated deployment (PXE-ready), but ISO-based workflows are fully supported.

---

## Features

- Automated Debian ISO generation  
- Verified downloads (GPG + SHA256)  
- Dynamic configuration with Jinja templates  
- Modular pipeline (download → verify → build)  
- Structured partitioning with LUKS + LVM  
- Automatic SSH key injection  
- Preseed-based unattended installation  
- PXE-ready deployment  
- Debian 13 (Trixie) support (extendable)  
- UEFI-only  

---

## Requirements

```bash
sudo apt install xorriso gnupg python3-venv
````

---

## Project Structure

```text
config/         → configuration files
assets/         → static files (grub, postinstall, recipes)
templates/      → Jinja templates
cache/          → temporary build data (auto-cleaned)
output/iso/     → generated ISO images
keys/           → GPG public keys
src/            → application source code
```

---

## Quick Start

### 1. Create a Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -e .
```

---

### 3. Configure environment variables

```bash
cp .env.example .env
```

Generate a password hash:

```bash
openssl passwd -6
```

---

### 4. Configure the system

```bash
cp config/example.yml config/default.yml
```

Edit `config/default.yml` and adjust values.

⚠️ All paths must be absolute.

---

### 5. Run the pipeline

```bash
python -m src.main
```

---

## How it works

The pipeline executes the following steps:

1. Build Debian ISO metadata
2. Download ISO + checksum files
3. Verify authenticity (GPG signature + SHA256)
4. Generate preseed configuration
5. Generate post-install scripts
6. Extract ISO and inject configuration
7. Rebuild final ISO image

---

## Security

* ISO integrity is verified using:

  * Debian CD signing keys (GPG)
  * SHA256 checksums
* No secrets are stored in the repository
* Sensitive data is injected via `.env`

---

## Output

Generated ISOs are stored in:

```text
output/iso/
```

---

## ⚠️ Warning

This tool performs fully automated installations and may **erase all data on target disks**.

Always test in a virtual machine before using on real hardware.

---

## Notes

* Only UEFI systems are supported
* Designed for reproducibility and offline usage
* Keys are stored locally and not fetched at runtime

```

---