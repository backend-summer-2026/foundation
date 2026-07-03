"""
DARS 2 — Mavzu 3.3: @classmethod va @staticmethod

    oddiy method  -> birinchi argument  self  (aniq obyekt bilan ishlaydi)
    @classmethod  -> birinchi argument  cls   (class bilan ishlaydi; ko'pincha "fabrika")
    @staticmethod -> maxsus argumentsiz (class ichidagi mustaqil yordamchi funksiya)
"""


class Sana:
    def __init__(self, kun, oy, yil):
        self.kun = kun
        self.oy = oy
        self.yil = yil

    def __str__(self):
        return f"{self.kun:02d}.{self.oy:02d}.{self.yil}"

    # classmethod — obyektni BOSHQACHA yo'l bilan yaratadigan "fabrika" metodi.
    @classmethod
    def matndan(cls, matn):
        """'03.07.2026' ko'rinishidagi matndan Sana obyekti yaratadi."""
        kun, oy, yil = matn.split(".")
        return cls(int(kun), int(oy), int(yil))   # cls == Sana

    # staticmethod — na self, na cls kerak. Class bilan mantiqan bog'liq,
    # lekin obyekt ma'lumotiga muhtoj bo'lmagan mustaqil funksiya.
    @staticmethod
    def kabisa_yilmi(yil):
        return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)


# 1) Oddiy yo'l — to'g'ridan konstruktor orqali.
s1 = Sana(3, 7, 2026)
print(s1)   # 03.07.2026

# 2) classmethod orqali — matndan qulay yaratish.
s2 = Sana.matndan("25.12.2025")
print(s2)   # 25.12.2025

# 3) staticmethod — obyekt yaratmasdan, to'g'ridan class orqali chaqiriladi.
print(Sana.kabisa_yilmi(2024))  # True
print(Sana.kabisa_yilmi(2026))  # False

# Qachon nima?
#   self mavjud obyekt ma'lumoti kerak bo'lsa        -> oddiy method
#   yangi obyekt yaratishning muqobil yo'li kerak    -> @classmethod
#   obyekt/class holatiga bog'liq bo'lmagan yordamchi -> @staticmethod

week_days = {0: "dushanba", 1: "seshanba", 5: "shanba"}


from datetime import datetime

text = "15.10.2022"
dt = datetime.strptime(text, "%d.%m.%Y")
week_days[dt.weekday()]
