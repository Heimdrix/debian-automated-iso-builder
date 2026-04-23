# Custom Debian ISO Generator for Automated Deployment (UEFI Only)

This project provides a Python-based pipeline to generate customized Debian ISO images for automated deployment.

It uses Jinja templating and a modular architecture to dynamically build installation media with reproducible and secure configurations.

The primary use case is ISO-based automated deployment. PXE workflows are supported but require manual kernel/initrd extraction.

---

## Features

- Automated Debian ISO generation  
- Verified downloads (GPG + SHA256)  
- Dynamic configuration with Jinja templates  
- Modular pipeline (download → verify → build)  
- Structured partitioning with LUKS + LVM  
- Automatic SSH key injection  
- Preseed-based unattended installation  
- PXE-compatible deployment (manual setup required)  
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

## PXE Usage (Optional)

To use the generated ISO in a PXE environment:

1. Extract kernel and initrd from the ISO:

   ```bash
   xorriso -osirrox on -indev custom.iso -extract / iso-root/
   ```

2. Use:

   ```text
   iso-root/install.amd/vmlinuz
   iso-root/install.amd/initrd.gz
   ```

3. Serve preseed over HTTP and configure boot parameters:

   ```text
   auto=true priority=critical preseed/url=http://server/preseed.cfg
   ```

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

---
