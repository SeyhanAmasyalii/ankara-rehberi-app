import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Lokanta:
    ad: str
    semt: str
    acilis: int
    kapanis: int


def lokantalari_yukle(dosya_yolu: str | Path) -> list[Lokanta]:
    """JSON dosyasindaki lokantalari dondurur; JSON listesi bossa [] dondurur."""
    with Path(dosya_yolu).open(encoding="utf-8") as dosya:
        veriler = json.load(dosya)
    return [Lokanta(**veri) for veri in veriler]
