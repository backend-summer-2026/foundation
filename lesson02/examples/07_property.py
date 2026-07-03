"""
DARS 2 — Mavzu 3.2: @property — getter / setter

@property attribute'ga o'xshab ishlaydigan method yaratadi.
Foyda: tashqaridan  obj.selsiy  deb oddiy attribute kabi yozamiz,
lekin ichida validatsiya yoki hisoblash yashiringan bo'ladi.
"""


class Harorat:
    def __init__(self, selsiy=0):
        self._selsiy = selsiy   # "_" — ichki (haqiqiy) saqlash joyi

    # GETTER — obj.selsiy O'QILGANDA ishlaydi.
    @property
    def selsiy(self):
        return self._selsiy

    # SETTER — obj.selsiy = ... YOZILGANDA ishlaydi (validatsiya shu yerda!).
    @selsiy.setter
    def selsiy(self, qiymat):
        if qiymat < -273.15:
            raise ValueError("Absolyut noldan past harorat bo'lishi mumkin emas")
        self._selsiy = qiymat

    # Hisoblanadigan property — hech qayerda saqlanmaydi, har safar hisoblanadi.
    @property
    def farengeyt(self):
        return self._selsiy * 9 / 5 + 32


h = Harorat(25)
print(h.selsiy)      # 25    -> getter ishladi (diqqat: () YO'Q, attribute kabi!)
print(h.farengeyt)   # 77.0  -> avtomatik hisoblandi

h.selsiy = 30        # setter ishladi
print(h.farengeyt)   # 86.0

# Noto'g'ri qiymatni setter to'xtatadi:
try:
    h.selsiy = -300
except ValueError as e:
    print("Xato ushlandi:", e)

# Xulosa: @property tashqi ko'rinishni SODDA (attribute kabi), ichki mantiqni
# esa XAVFSIZ (nazorat qilingan) qiladi — ikkalasi birga.
