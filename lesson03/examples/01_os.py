"""
DARS 3 — Standart kutubxona: os

    os moduli — operatsion tizim bilan ishlash: papka/fayl yo'llari,
    papka yaratish, muhit o'zgaruvchilari (environment variables).

Loyihada eng ko'p ishlatiladigan qismlar:
    os.getenv(...)        -> maxfiy sozlama (token, parol) o'qish
    os.makedirs(...)      -> natija/hisobot papkasini yaratish
    os.path.join(...)     -> yo'llarni to'g'ri birlashtirish (OS ga bog'liq emas)
    os.path.exists(...)   -> fayl/papka bor-yo'qligini tekshirish

Ishga tushiring:  python 01_os.py
"""
import os

# --- 1. Muhit o'zgaruvchisi (environment variable) ---
# Loyihada BOT_TOKEN, DATABASE_URL kabi maxfiy qiymatlar shu yerdan o'qiladi.
# 2-argument — standart (default) qiymat: o'zgaruvchi topilmasa shu qaytadi.
token = os.getenv("BOT_TOKEN", "token-topilmadi")
print("BOT_TOKEN:", token)

# --- 2. Joriy ishchi papka (qayerda turibmiz) ---
print("Joriy papka:", os.getcwd())

# --- 3. Yo'llarni to'g'ri birlashtirish ---
# "hisobotlar" + "yanvar.txt" -> mac/Linux'da "/", Windows'da "\" ni o'zi qo'yadi.
papka = "hisobotlar"
fayl_yoli = os.path.join(papka, "yanvar.txt")
print("To'liq yo'l:", fayl_yoli)

# --- 4. Papka yaratish (bor bo'lsa xato bermaydi) ---
os.makedirs(papka, exist_ok=True)   # exist_ok=True -> mavjud bo'lsa jim o'tadi
print(f"'{papka}' papkasi tayyor.")

# --- 5. Fayl/papka bor-yo'qligini tekshirish ---
print("Papka mavjudmi?", os.path.exists(papka))
print("Fayl mavjudmi?", os.path.exists(fayl_yoli))

# --- 6. Papka ichidagi fayllar ro'yxati ---
print("Papka ichidagilar:", os.listdir(papka))

# DIQQAT: bugungi kunda yo'llar bilan ishlashda ko'pincha os.path o'rniga
# zamonaviy 'pathlib' ishlatiladi (keyingi misol: 02_pathlib.py).
