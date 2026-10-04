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
    if lokanta.acilis <= lokanta.kapanis:
        return lokanta.acilis <= saat < lokanta.kapanis
    else:
        return saat >= lokanta.acilis or saat < lokanta.kapanis

if __name__ == "__main__":
    kebapci = Lokanta("Kebapci Iskender", "Kizilay", 11, 22)
    meyhane = Lokanta("Gece Lokantasi", "Ulus", 18, 2)

    print("Kebapci 12:00 ->", acik_mi(kebapci, 12))   # True olmali
    print("Kebapci 23:00 ->", acik_mi(kebapci, 23))   # False olmali
    print("Meyhane 01:00 ->", acik_mi(meyhane, 1))    # True olmali  (gece yarisini geciyor)
    print("Meyhane 10:00 ->", acik_mi(meyhane, 10))   # False olmali
    print("Meyhane 02:00 ->", acik_mi(meyhane, 2))    # ? kapanis saatinde acik mi?

    