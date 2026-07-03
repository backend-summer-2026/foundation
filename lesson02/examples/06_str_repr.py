"""
DARS 2 — Mavzu 3.1: Maxsus (dunder) metodlar — __str__ va __repr__

dunder = "double underscore" (__nom__). Python ularni maxsus holatlarda
AVTOMATIK chaqiradi (siz to'g'ridan chaqirmaysiz).

    __str__  -> print() va str() uchun — foydalanuvchiga chiroyli ko'rinish
    __repr__ -> dasturchi uchun — aniq, "texnik" ko'rinish (debug uchun)
"""



class Kitob:
    def __init__(self, nom, muallif, narx):
        self.nom = nom
        self.muallif = muallif
        self.narx = narx

    # print(kitob) shu metodni chaqiradi.
    def __str__(self):
        return f"'{self.nom}' — {self.muallif}"

    # repr(kitob), yoki obyekt ro'yxat ichida bo'lsa — shu chaqiriladi.
    def __repr__(self):
        return f"Kitob(nom={self.nom!r}, muallif={self.muallif!r}, narx={self.narx})"

    # kitob1 == kitob2 solishtiruvini boshqaradi.
    def __eq__(self, other):
        return self.nom == other.nom and self.muallif == other.muallif

    # len(kitob) -> bu yerda nom uzunligini qaytaradi.
    def __len__(self):
        return len(self.nom)

    # add dunder method
    def __add__(self, other):
        return Kitob(
            self.nom + other.nom,
            self.muallif + other.muallif,
            self.narx + other.narx
        )


k1 = Kitob("Otkan kunlar", "A. Qodiriy", 45000)
k2 = Kitob("Otkan kunlar", "A. Qodiriy", 50000)

# print(dir(k1))

print(k1)          # __str__  -> 'Otkan kunlar' — A. Qodiriy
print(str(k1))     # __str__  -> yuqoridagi bilan bir xil
print(repr(k1))    # __repr__ -> Kitob(nom='Otkan kunlar', ...)
print([k1, k2])    # ro'yxat ICHIDA __repr__ ishlaydi

print(k1 == k2)    # __eq__  -> True (nom + muallif bir xil, narx muhim emas)
print(k2 == k1)    # __eq__  -> True (nom + muallif bir xil, narx muhim emas)
print(len(k1))     # __len__ -> 12

# Agar __str__ / __repr__ yozmasak, print(obyekt) shunday chiqadi:
#   <__main__.Kitob object at 0x7f...>   — o'qib bo'lmaydigan, foydasiz.

k = k1 + k2 # k1.__add__(k2) -> k
print(k.narx)

num1 = 2
num2 = 5

num = num1 + num2 # num1.__add__(num2) -> num
