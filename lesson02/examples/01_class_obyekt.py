"""
DARS 2 — Mavzu 1: OOP asoslari
Class, obyekt, __init__, self, attribute va method.

Ishga tushirish:  python 01_class_obyekt.py
"""


# --- 1. Class (klass) — obyekt uchun "chizma" (blueprint) ---
class Mahsulot:
    """Do'kondagi bitta mahsulotni ifodalaydi."""

    # Class attribute — barcha obyektlar uchun umumiy (bitta nusxa).
    valyuta = "so'm"

    # __init__ — konstruktor. Obyekt yaratilganda AVTOMATIK chaqiriladi.
    # self — hozir yaratilayotgan obyektning o'zini bildiradi.
    def __init__(self, nom, narx, miqdor):
        # Instance attribute — har bir obyektning O'Z ma'lumoti.
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor

    # Method — obyektning xatti-harakati (class ichidagi funksiya).
    def umumiy_narx(self):
        return self.narx * self.miqdor

    def chegirma_ber(self, foiz):
        """Narxni berilgan foizga kamaytiradi."""
        self.narx = self.narx - (self.narx * foiz / 100)


# --- 2. Obyekt (instance) yaratish ---
# Mahsulot(...) chaqirilganda __init__ ishga tushadi.
olma = Mahsulot("Olma", 12000, 3)
non = Mahsulot("Non", 4000, 10)

# --- 3. Attribute'ga murojaat ---``
print("--- Instance attribute ---")
print(olma.nom)          # Olma
print(olma.narx)         # 12000

print("--- Class attribute ---")
# Mahsulot.valyuta = "USD"  # class attribute o'zgartirish
print(Mahsulot.valyuta)  # USD  (class attribute)
print(non.valyuta)       # USD  (class attribute)
print(olma.valyuta)      # USD  (class attribute)

# --- 4. Method chaqirish ---
print("--- Method chaqirish ---")
print(olma.umumiy_narx())   # 36000
print(non.umumiy_narx())    # 40000

# olma va non — ALOHIDA obyektlar, har biri o'z ma'lumotiga ega.
olma.chegirma_ber(10)
print(olma.narx)   # 10800.0  (faqat olma o'zgardi)
print(non.narx)    # 4000     (non o'zgarmadi)

# Xulosa:
#   class     -> umumiy shablon
#   obyekt    -> shablondan yaratilgan aniq nusxa
#   __init__  -> obyekt tug'ilganda ishlaydigan sozlash
#   self      -> "shu obyekt"
#   attribute -> ma'lumot (nom, narx)
#   method    -> harakat (umumiy_narx, chegirma_ber)
