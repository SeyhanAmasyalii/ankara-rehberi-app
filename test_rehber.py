import pytest

from rehber import Lokanta, acik_mi, acik_olanlar, en_erken_acilan


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


def test_en_erken_acilan_lokantanin_adini_doner():
    gece_lokantasi = Lokanta("Gece Lokantasi", "Ulus", 18, 2)
    sabah_lokantasi = Lokanta("Sabah Lokantasi", "Cankaya", 8, 14)
    kebapci = Lokanta("Kebapci", "Kizilay", 11, 22)

    assert en_erken_acilan([gece_lokantasi, kebapci, sabah_lokantasi]) == "Sabah Lokantasi"


def test_en_erken_acilan_bos_liste_icin_none_doner():
    assert en_erken_acilan([]) is None


def test_en_erken_acilan_esit_saatte_ilk_lokantayi_doner():
    ilk_lokanta = Lokanta("Ilk Lokanta", "Kizilay", 8, 14)
    ikinci_lokanta = Lokanta("Ikinci Lokanta", "Ulus", 8, 18)

    assert en_erken_acilan([ilk_lokanta, ikinci_lokanta]) == "Ilk Lokanta"
