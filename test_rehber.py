import pytest

from rehber import Lokanta, acik_mi, acik_olanlar


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


def test_saat_birde_sadece_gece_lokantasi_doner():
    gece_lokantasi = Lokanta("Gece Lokantasi", "Ulus", 18, 2)
    kebapci = Lokanta("Kebapci", "Kizilay", 9, 17)

    assert acik_olanlar([kebapci, gece_lokantasi], 1) == ["Gece Lokantasi"]


def test_saat_on_ikide_kebapci_doner():
    gece_lokantasi = Lokanta("Gece Lokantasi", "Ulus", 18, 2)
    kebapci = Lokanta("Kebapci", "Kizilay", 9, 17)

    assert acik_olanlar([gece_lokantasi, kebapci], 12) == ["Kebapci"]


def test_acik_lokanta_yoksa_bos_liste_doner():
    lokantalar = [
        Lokanta("Kebapci", "Kizilay", 9, 17),
        Lokanta("Gece Lokantasi", "Ulus", 18, 2),
    ]

    assert acik_olanlar(lokantalar, 8) == []


def test_acik_lokantalar_alfabetik_siralanir():
    zeytin = Lokanta("Zeytin", "Bahceli", 9, 17)
    ada = Lokanta("Ada", "Kizilay", 9, 17)
    kebapci = Lokanta("Kebapci", "Ulus", 9, 17)

    assert acik_olanlar([zeytin, kebapci, ada], 12) == ["Ada", "Kebapci", "Zeytin"]


