# Ankara Rehberi web arama sayfasi
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/ara")
def ara() -> str:
    """Lokanta adina gore arama yapar."""
    ad = request.args.get("ad", "")
    baglanti = sqlite3.connect("rehber.db")
    sonuc = baglanti.execute("SELECT * FROM lokanta WHERE ad = ?", (ad,)).fetchall()
    return str(sonuc)


if __name__ == "__main__":
    app.run()