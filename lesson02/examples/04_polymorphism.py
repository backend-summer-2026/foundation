"""
DARS 2 — Mavzu 2.3: Polymorphism (ko'p shakllilik)

Bir xil nomli method turli classlarda turlicha ishlaydi.
Natijada: bitta funksiya obyekt turini bilmasdan ular bilan ishlay oladi.
"Duck typing": obyekt nima EKANI emas, nima QILA OLISHI muhim.
"""


# --- Umumiy shablon (baza) ---
class Tolov:
    def bajar(self):
        raise NotImplementedError("Har bir to'lov turi bajar() ni yozishi shart")


class Naqd(Tolov):
    def __init__(self, summa):
        self.summa = summa

    def bajar(self):
        return f"Naqd pul bilan {self.summa} so'm to'landi"


class Karta(Tolov):
    def __init__(self, summa, raqam):
        self.summa = summa
        self.raqam = raqam

    def bajar(self):
        return f"Karta (*{self.raqam[-4:]}) orqali {self.summa} so'm to'landi"


class Click(Tolov):
    def __init__(self, summa):
        self.summa = summa

    def bajar(self):
        return f"Click orqali {self.summa} so'm to'landi"


# Bitta funksiya — istalgan to'lov turi bilan ishlaydi.
# Har bir obyekt O'ZINING bajar() metodini chaqiradi.
def tolovni_amalga_oshir(tolov: Tolov):
    print(tolov.bajar())


tolovlar = [
    Naqd(50000),
    Karta(120000, "8600123456781234"),
    Click(30000),
]

# Bir xil chaqiruv (tolov.bajar()) — turli natija. Mana shu polimorfizm.
for t in tolovlar:
    tolovni_amalga_oshir(t)

# Qo'shimcha: Python'da ko'p standart amallar ham polimorfik:
print(len("salom"))       # 5   -> string uzunligi
print(len([1, 2, 3]))     # 3   -> list uzunligi
print(3 + 4)              # 7   -> qo'shish
print("3" + "4")          # 34  -> ulash (bir xil "+", turli xatti-harakat)
