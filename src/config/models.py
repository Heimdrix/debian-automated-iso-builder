from pathlib import Path
from pydantic import BaseModel, Field


class DiskConfig(BaseModel):
    luks_passphrase: str = Field(min_length=1)
    target_device: str = Field(pattern=r"^/dev/")


class IsoConfig(BaseModel):
    arch: str = Field(min_length=1)
    version: str = Field(min_length=1)


class NetworkConfig(BaseModel):
    domain: str = Field(min_length=1)
    hostname: str = Field(min_length=1)


class OpenSSHConfig(BaseModel):
    public_key_path: Path


class PackagesConfig(BaseModel):
    exclude: list[str] = Field(default_factory=list)
    include: list[str] = Field(default_factory=list)


class PreseedConfig(BaseModel):
    recipe_path: Path


class SystemConfig(BaseModel):
    keymap: str = Field(min_length=1)
    locale: str = Field(min_length=1)
    timezone: str = Field(min_length=1)


class UserConfig(BaseModel):
    password_hash: str = Field(min_length=1)
    username: str = Field(min_length=1)


class Config(BaseModel):
    disk: DiskConfig
    iso: IsoConfig
    network: NetworkConfig
    openssh: OpenSSHConfig
    packages: PackagesConfig
    preseed: PreseedConfig
    system: SystemConfig
    user: UserConfig