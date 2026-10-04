import pytest

from rehber import Lokanta, acik_mi


@pytest.mark.parametrize(
    ("saat", "beklenen"),
    [
        (10, False),
        (11, True),
        (12, True),
        (21, True),
        (22, False),
    ],
)
def test_normal_saatlerde_acilis_dahil_kapanis_haric(saat, beklenen):
    lokanta = Lokanta("Gunduz Lokantasi", "Kizilay", 11, 22)

    assert acik_mi(lokanta, saat) is beklenen


@pytest.mark.parametrize(
    ("saat", "beklenen"),
    [
        (17, False),
        (18, True),
        (23, True),
        (0, True),
        (1, True),
        (2, False),
        (3, False),
    ],
)
def test_gece_yarisini_gecen_saatlerde_acilis_dahil_kapanis_haric(saat, beklenen):
    lokanta = Lokanta("Gece Lokantasi", "Ulus", 18, 2)

    assert acik_mi(lokanta, saat) is beklenen

def test_yedi_yirmi_dort_acik():
    kafe = Lokanta("7/24 Kafe", "Cankaya", 0, 0)
    assert acik_mi(kafe, 15) is True
