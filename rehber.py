# Ankara Rehberi: lokantalarin acik olup olmadigini hesaplar
from dataclasses import dataclass


@dataclass
class Lokanta:
    ad: str
    semt: str
    acilis: int   # saat, 0-23
    kapanis: int  # saat, 0-23


def acik_mi(lokanta: Lokanta, saat: int) -> bool:
    """Verilen saatte lokanta acik mi? Gece yarisini gecen saatleri de destekler (orn. 18-02)."""
    if lokanta.acilis == lokanta.kapanis:
        return True
    if lokanta.acilis <= lokanta.kapanis:
        return lokanta.acilis <= saat < lokanta.kapanis
    else:
        return saat >= lokanta.acilis or saat < lokanta.kapanis


def acik_olanlar(lokantalar: list[Lokanta], saat: int) -> list[str]:
    """Verilen saatte acik olan lokantalarin adlarini alfabetik sirayla dondurur."""
    return sorted(lokanta.ad for lokanta in lokantalar if acik_mi(lokanta, saat))


def en_erken_acilan(lokantalar: list[Lokanta]) -> str | None:
    """En erken acilan lokantanin adini; liste bossa None dondurur."""
    if not lokantalar:
        return None
    return min(lokantalar, key=lambda lokanta: lokanta.acilis).ad



if __name__ == "__main__":
    lokantalar = [
        Lokanta("Kebapci Iskender", "Kizilay", 11, 22),
        Lokanta("Gece Lokantasi", "Ulus", 18, 2),
        Lokanta("Sabah Lokantasi", "Cankaya", 8, 14),
    ]

    print("01:00'de acik lokantalar:", acik_olanlar(lokantalar, 1))

    