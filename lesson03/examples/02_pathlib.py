"""
DARS 3 — Standart kutubxona: pathlib  ⭐ (zamonaviy usul)

    pathlib — fayl yo'llari bilan OBYEKT ko'rinishida ishlash.
    os.path'ning zamonaviy, o'qishga qulay o'rnini bosuvchisi.

    Path("papka") / "fayl.txt"   <- yo'llarni "/" bilan birlashtiramiz (chiroyli!)

Loyihada eng ko'p ishlatiladigan qismlar:
    Path(__file__).parent   -> shu skript turgan papka (ildiz yo'lini topish)
    p.mkdir(...)            -> papka yaratish
    p.write_text / read_text -> faylni bir qatorda yozish / o'qish
    p.exists(), p.glob(...) -> tekshirish, bir turdagi fayllarni yig'ish

Ishga tushiring:  python 02_pathlib.py
"""
from pathlib import Path

# --- 1. Shu skript turgan papkani topish (loyiha ildizi) ---
# __file__ -> shu fayl yo'li; .parent -> uni o'rab turgan papka.
BASE_DIR = Path(__file__).parent
print("Loyiha papkasi:", BASE_DIR)

# --- 2. Yo'llarni "/" operatori bilan birlashtirish ---
hisobot_papka = BASE_DIR / "hisobotlar"
fayl = hisobot_papka / "yanvar.txt"
print("Hisobot fayli:", fayl)

# --- 3. Papka yaratish ---
# parents=True -> oraliq papkalarni ham yaratadi; exist_ok=True -> bor bo'lsa jim.
hisobot_papka.mkdir(parents=True, exist_ok=True)

# --- 4. Faylga YOZISH va o'qish (bitta qatorda, open() shart emas!) ---
fayl.write_text("Olma - 12000\nNon - 4000\n", encoding="utf-8")
matn = fayl.read_text(encoding="utf-8")
print("--- Fayl mazmuni ---")
print(matn)

# --- 5. Yo'lning bo'laklari ---
print("Fayl nomi:", fayl.name)        # yanvar.txt
print("Kengaytma:", fayl.suffix)      # .txt
print("Nomi (kengaytmasiz):", fayl.stem)  # yanvar
print("Papkasi:", fayl.parent)

# --- 6. Bir turdagi fayllarni yig'ish (glob) ---
# "*.txt" -> papkadagi barcha .txt fayllar.
txt_fayllar = list(hisobot_papka.glob("*.txt"))
print("Papkadagi .txt fayllar:", [f.name for f in txt_fayllar])

# --- 7. Tekshirish ---
print("Fayl bormi?", fayl.exists())
print("Papkami?", hisobot_papka.is_dir())

# XULOSA: pathlib os.path'dan o'qishga qulayroq va xatoga kam moyil.
# Yangi loyihalarda yo'llar uchun pathlib'ni tavsiya qilamiz.
