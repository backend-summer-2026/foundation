"""
DARS 3 — Standart kutubxona: random

    random — tasodifiy qiymatlar.
    Loyihada: test (soxta) ma'lumot yaratish, tasodifiy tanlov, tartibni aralashtirish,
    tasodifiy kod/parol qismi.

Loyihada eng ko'p ishlatiladigan qismlar:
    random.randint(a, b)   -> a va b orasidagi butun son (ikkalasi ham kiradi)
    random.choice(ro'yxat) -> ro'yxatdan bitta tasodifiy element
    random.sample(ro'yxat, k) -> takrorsiz k ta element
    random.shuffle(ro'yxat) -> ro'yxatni joyida aralashtiradi
    random.seed(n)         -> natijani takrorlanadigan qiladi (test uchun)

Ishga tushiring:  python 05_random.py
"""
import random

# --- 0. seed — bir xil natija chiqishi uchun (testda foydali) ---
# Buni izohga olsangiz, har safar boshqa natija chiqadi.
random.seed(42)

mahsulotlar = ["Olma", "Non", "Sut", "Guruch", "Choy"]

# --- 1. Tasodifiy butun son (masalan: soni yoki narx) ---
print("Tasodifiy son (1-10):", random.randint(1, 10))

# --- 2. Ro'yxatdan bitta tasodifiy element ---
print("Tasodifiy mahsulot:", random.choice(mahsulotlar))

# --- 3. Takrorsiz bir nechta element (sample) ---
print("3 ta har xil mahsulot:", random.sample(mahsulotlar, 3))

# --- 4. Ro'yxatni aralashtirish (shuffle — joyida o'zgartiradi) ---
nusxa = mahsulotlar.copy()
random.shuffle(nusxa)
print("Aralashtirilgan:", nusxa)

# --- 5. Kasrli tasodifiy son (masalan: chegirma foizi) ---
print("Tasodifiy kasr (0-1):", round(random.random(), 2))

# --- 6. AMALIY: soxta (test) buyurtmalar yaratish ---
# Loyihani sinash uchun tez ma'lumot generatsiya qilamiz.
print("\n--- Soxta buyurtmalar ---")
for i in range(1, 6):
    buyurtma = {
        "id": i,
        "mahsulot": random.choice(mahsulotlar),
        "soni": random.randint(1, 20),
        "narx": random.choice([4000, 9000, 12000, 25000]),
    }
    print(buyurtma)

# DIQQAT: random parol/token uchun XAVFSIZ EMAS. Maxfiy kod kerak bo'lsa
# 'secrets' modulini ishlating (secrets.token_hex()).
