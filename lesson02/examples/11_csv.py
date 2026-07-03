"""
DARS 2 — Mavzu 5 (qo'shimcha): CSV bilan tanishish

CSV (Comma-Separated Values) — jadval ko'rinishidagi ma'lumot (Excel ochadi).
Har bir qator = bitta yozuv, ustunlar vergul bilan ajratiladi.

`csv` moduli:
    csv.writer / csv.reader          -> oddiy ro'yxat (list) bilan
    csv.DictWriter / csv.DictReader  -> dict bilan (ustun nomlari bo'yicha) — qulayroq

Ishga tushirilganda shu papkada 'mahsulotlar.csv' fayli yaratiladi.
"""

import csv

# --- 1. CSV faylga YOZISH (DictWriter) ---
mahsulotlar = [
    {"nom": "Olma", "narx": 12000, "miqdor": 3},
    {"nom": "Non", "narx": 4000, "miqdor": 10},
    {"nom": "Sut", "narx": 9000, "miqdor": 5},
]

# newline="" -> Windows'da ortiqcha bo'sh qatorlar chiqmasligi uchun (CSV qoidasi).
with open("mahsulotlar.csv", "w", encoding="utf-8", newline="") as f:
    ustunlar = ["nom", "narx", "miqdor"]
    writer = csv.DictWriter(f, fieldnames=ustunlar)
    writer.writeheader()            # 1-qator: ustun nomlari (nom,narx,miqdor)
    writer.writerows(mahsulotlar)   # qolgan qatorlar
print("CSV saqlandi")

# --- 2. CSV fayldan O'QISH (DictReader) ---
print("--- O'qildi ---")
with open("mahsulotlar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for qator in reader:
        # DIQQAT: CSV'dan hamma qiymat STRING bo'lib keladi -> int() bilan o'giramiz.
        summa = int(qator["narx"]) * int(qator["miqdor"])
        print(f"{qator['nom']}: {summa} so'm")

# JSON va CSV farqi:
#   JSON -> murakkab/ichma-ich (nested) ma'lumot, API'lar uchun.
#   CSV  -> oddiy jadval (ustun/qator), Excel va hisobotlar uchun.
