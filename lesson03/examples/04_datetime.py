"""
DARS 3 — Standart kutubxona: datetime

    datetime — sana va vaqt bilan ishlash.
    Loyihada: hisobot sanasi, log vaqti, fayl nomiga timestamp, "necha kun oldin".

Loyihada eng ko'p ishlatiladigan qismlar:
    datetime.now()          -> hozirgi sana-vaqt
    .strftime("%Y-%m-%d")   -> sanani MATNGA aylantirish (formatlash)
    strptime(matn, format)  -> matndan sanani O'QISH (aksincha)
    date2 - date1           -> ikki sana orasidagi farq (timedelta)

Ishga tushiring:  python 04_datetime.py
"""
from datetime import datetime, date, timedelta

# --- 1. Hozirgi sana va vaqt ---
hozir = datetime.now()
print("Hozir:", hozir)

# --- 2. Sanani formatlash (strftime) — hisobot/log uchun ---
#   %Y=yil  %m=oy  %d=kun   %H=soat  %M=daqiqa  %S=soniya
print("Sana:", hozir.strftime("%Y-%m-%d"))
print("Vaqt:", hozir.strftime("%H:%M:%S"))

# Log qatori namunasi:
print(f"[{hozir.strftime('%Y-%m-%d %H:%M:%S')}] Hisobot yaratildi")

# Faylga timestamp qo'shish (bir xil nom ustiga yozib yubormaslik uchun):
fayl_nomi = f"hisobot_{hozir.strftime('%Y%m%d_%H%M%S')}.txt"
print("Fayl nomi:", fayl_nomi)

# --- 3. Matndan sanani o'qish (strptime) ---
# Foydalanuvchi yoki fayldan kelgan matnni sanaga aylantiramiz.
matn = "2026-01-15"
buyurtma_sanasi = datetime.strptime(matn, "%Y-%m-%d").date()
print("O'qilgan sana:", buyurtma_sanasi)

# --- 4. Sanalar farqi (timedelta) — "necha kun o'tdi" ---
bugun = date.today()
farq = bugun - buyurtma_sanasi
print(f"Buyurtmadan beri {farq.days} kun o'tdi")

# --- 5. Kelajak/o'tmish sanani hisoblash ---
etkazish = bugun + timedelta(days=3)   # 3 kundan keyin
print("Yetkazib berish sanasi:", etkazish)

hafta_oldin = bugun - timedelta(days=7)
print("Bir hafta oldin:", hafta_oldin)

# ESLATMA: server/baza uchun ko'pincha UTC vaqti ishlatiladi:
#   datetime.now(timezone.utc)  (timezone'ni datetime'dan import qilib).
