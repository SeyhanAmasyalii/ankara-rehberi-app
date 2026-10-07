import json
from pathlib import Path

from veri import Lokanta, lokantalari_yukle


def test_lokantalari_yukle_jsondaki_kayitlari_lokanta_yapar(tmp_path: Path) -> None:
    dosya_yolu = tmp_path / "lokantalar.json"
    dosya_yolu.write_text(
        json.dumps(
            [
                {
                    "ad": "Deneme Lokantasi",
                    "semt": "Kizilay",
                    "acilis": 9,
                    "kapanis": 17,
                }
            ]
        ),
        encoding="utf-8",
    )

    assert lokantalari_yukle(dosya_yolu) == [
        Lokanta("Deneme Lokantasi", "Kizilay", 9, 17)
    ]


def test_lokantalari_yukle_bos_json_listesi_icin_bos_liste_doner(
    tmp_path: Path,
) -> None:
    dosya_yolu = tmp_path / "lokantalar.json"
    dosya_yolu.write_text("[]", encoding="utf-8")

    assert lokantalari_yukle(dosya_yolu) == []


def test_lokantalari_yukle_proje_jsonunda_bes_lokanta_bulunur() -> None:
    dosya_yolu = Path(__file__).with_name("lokantalar.json")

    lokantalar = lokantalari_yukle(dosya_yolu)

    assert len(lokantalar) == 5
    assert any(lokanta.acilis > lokanta.kapanis for lokanta in lokantalar)
    assert any(lokanta.acilis == lokanta.kapanis for lokanta in lokantalar)
