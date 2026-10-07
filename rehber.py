# Ankara Rehberi: lokantalarin acik olup olmadigini hesaplar
import argparse
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from veri import Lokanta, lokantalari_yukle

# Is kurali: saatler Turkiye saatine gore hesaplanir (sunucu UTC olsa bile).
TURKIYE = ZoneInfo("Europe/Istanbul")


def acik_mi(lokanta: Lokanta, saat: int) -> bool:
    """Verilen saatte lokanta acik mi? Gece yarisini gecen saatleri de destekler (orn. 18-02)."""
    if lokanta.acilis == lokanta.kapanis:
        return True
    if lokanta.acilis <= lokanta.kapanis:
        return lokanta.acilis <= saat < lokanta.kapanis
    else:
        return saat >= lokanta.acilis or saat < lokanta.kapanis


def acik_olanlar(lokantalar: list[Lokanta], saat: int) -> list[str]:
    """Acik lokanta adlarini sirali dondurur; lokanta listesi bossa [] dondurur."""
    return sorted(lokanta.ad for lokanta in lokantalar if acik_mi(lokanta, saat))


def en_erken_acilan(lokantalar: list[Lokanta]) -> str | None:
    """En erken acilan lokantanin adini; liste bossa None dondurur."""
    if not lokantalar:
        return None
    return min(lokantalar, key=lambda lokanta: lokanta.acilis).ad


def main(argv: list[str] | None = None, simdi: datetime | None = None) -> int:
    """Komut satirindan secilen saatte acik olan lokantalari listeler."""
    parser = argparse.ArgumentParser(description="Ankara'daki acik lokantalari listele.")
    parser.add_argument(
        "--saat",
        type=int,
        choices=range(24),
        help="Kontrol edilecek saat (0-23); verilmezse su anki saat kullanilir.",
    )
    args = parser.parse_args(argv)

    saat = args.saat if args.saat is not None else (simdi or datetime.now(TURKIYE)).hour
    lokantalar = lokantalari_yukle(Path(__file__).with_name("lokantalar.json"))
    acik_lokantalar = acik_olanlar(lokantalar, saat)
    print(f"{saat:02d}:00'de acik lokantalar:")
    if acik_lokantalar:
        for ad in acik_lokantalar:
            print(f"- {ad}")
    else:
        print("- Acik lokanta yok.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())