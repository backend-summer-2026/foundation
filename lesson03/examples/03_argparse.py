"""
DARS 3 — Standart kutubxona: argparse

    argparse — terminaldan dasturga ARGUMENT berish uchun.
    Kodni har safar tahrirlamasdan, tashqaridan sozlaymiz.

    Masalan "Buyurtmalar tahlilchisi" ni turli oyga ishga tushirish:
        python 03_argparse.py --oy yanvar --limit 5

Loyihada eng ko'p ishlatiladigan qismlar:
    add_argument("--nom")            -> ixtiyoriy nomli argument
    add_argument("fayl")             -> majburiy (pozitsion) argument
    type=int / default=... / help=.. -> tur, standart qiymat, izoh
    action="store_true"              -> bayroq (bor/yo'q: --debug)

Ishga tushiring (bir nechta variant):
    python 03_argparse.py buyurtmalar.json
    python 03_argparse.py buyurtmalar.json --oy yanvar --limit 3
    python 03_argparse.py --help          <- avtomatik yordam matni
"""
import argparse

# --- 1. Parser (argument o'qiydigan obyekt) yaratamiz ---
parser = argparse.ArgumentParser(
    description="Buyurtmalar tahlilchisi — CLI namunasi"
)

# --- 2. Argumentlarni e'lon qilamiz ---

# Pozitsion (majburiy) argument — nomsiz beriladi:
parser.add_argument("fayl", help="Buyurtmalar fayli yo'li (masalan: buyurtmalar.json)")

# Ixtiyoriy nomli argument (standart qiymati bor):
parser.add_argument("--oy", default="yanvar", help="Hisobot oyi (default: yanvar)")

# Butun son turidagi argument:
parser.add_argument("--limit", type=int, default=10, help="Nechta natija ko'rsatilsin")

# Bayroq (flag) — berilsa True, berilmasa False:
parser.add_argument("--debug", action="store_true", help="Batafsil (debug) rejim")

# --- 3. Argumentlarni o'qiymiz ---
args = parser.parse_args()

# --- 4. Ishlatamiz ---
print("Fayl:  ", args.fayl)
print("Oy:    ", args.oy)
print("Limit: ", args.limit)
print("Debug: ", args.debug)

if args.debug:
    print("[debug] Tahlil boshlandi... barcha qadamlar loglanadi.")

print(f"\n'{args.fayl}' faylidan {args.oy} oyi uchun "
      f"eng yuqori {args.limit} ta buyurtma tahlil qilinadi.")

# FOYDA: --help ni argparse O'ZI hosil qiladi. Xato argument berilsa,
# tushunarli xabar chiqaradi. Professional CLI dasturlar shunday yoziladi.
