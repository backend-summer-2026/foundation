"""
DARS 2 — Mavzu 4: Fayllar bilan ishlash

    open(fayl, rejim, encoding)
      "r" -> o'qish (read)       "w" -> yozish (mavjud matnni O'CHIRIB qayta yozadi)
      "a" -> qo'shish (append)   "x" -> yangi fayl yaratish (bor bo'lsa xato)

    with — context manager: blok tugagach fayl AVTOMATIK yopiladi (xato bo'lsa ham).
    Har doim  encoding="utf-8"  ishlating (lotin/kirill/emoji to'g'ri saqlanadi).

Ishga tushirilganda shu papkada 'mahsulotlar.txt' fayli yaratiladi.
"""
import time


# --- 1. Faylga YOZISH ("w" — eski mazmunni o'chiradi) ---
with open("mahsulotlar.txt", "w", encoding="utf-8") as f:
    f.write("Olma - 12000\n")   # \n -> yangi qator
    f.write("Non - 4000\n")
# with bloki tugadi -> fayl avtomatik yopildi (f.close() SHART emas)

time.sleep(3)
# --- 2. Faylga QO'SHISH ("a" — oxiriga qo'shadi, o'chirmaydi) ---
with open("mahsulotlar.txt", "a", encoding="utf-8") as f:
    f.write("Sut - 9000\n")


time.sleep(3)
# --- 3. Faylni TO'LIQ o'qish ("r") ---
with open("mahsulotlar.txt", "r", encoding="utf-8") as f:
    matn = f.read()
print("--- To'liq matn ---")
print(matn)


time.sleep(3)
# --- 4. QATORMA-QATOR o'qish (katta fayllar uchun tejamli) ---
print("--- Qayta ishlangan ---")
with open("mahsulotlar.txt", "r", encoding="utf-8") as f:
    for qator in f:
        nom, narx = qator.strip().split(" - ")   # strip() -> \n ni olib tashlaydi
        print(f"{nom}: {int(narx)} so'm")


time.sleep(3)
# --- 5. Barcha qatorlarni RO'YXAT sifatida olish ---
with open("mahsulotlar.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()
print(f"\nJami {len(qatorlar)} ta qator")

# DIQQAT: "w" rejimi faylni butunlay tozalaydi. Mavjud ma'lumotni saqlab
# qo'shmoqchi bo'lsangiz — "a" (append) rejimidan foydalaning.
