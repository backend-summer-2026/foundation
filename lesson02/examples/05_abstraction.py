"""
DARS 2 — Mavzu 2.4: Abstraction (abstraksiya)

Abstract class — to'g'ridan-to'g'ri obyekt yaratib bo'lmaydigan "shablon".
U faqat qanday methodlar BO'LISHI shartligini belgilaydi (majburiy shartnoma),
lekin ularni qanday bajarishni bolalar classiga qoldiradi.
`abc` (Abstract Base Class) moduli bilan yoziladi.
"""

from abc import ABC, abstractmethod


class Figura(ABC):
    """Barcha figuralar uchun umumiy shartnoma."""

    @abstractmethod
    def yuza(self):
        """Har bir figura O'ZINING yuzasini hisoblashi SHART."""
        ...

    @abstractmethod
    def perimetr(self):
        ...

    # Abstract class oddiy (tayyor) methodga ham ega bo'lishi mumkin.
    def malumot(self):
        return f"Yuza = {self.yuza():.2f}, Perimetr = {self.perimetr():.2f}"


class Tortburchak(Figura):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return self.eni * self.boyi

    def perimetr(self):
        return 2 * (self.eni + self.boyi)


class Doira(Figura):
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return self.PI * self.radius ** 2

    def perimetr(self):
        return 2 * self.PI * self.radius


# f = Figura()   # -> TypeError: abstract class'dan obyekt yaratib bo'lmaydi!

figuralar = [Tortburchak(4, 5), Doira(3)]
for f in figuralar:
    print(f.malumot())

# Xulosa: abstraksiya "NIMA qilinishi kerak"ni belgilaydi,
# har bir class esa "QANDAY qilinishini" o'zi hal qiladi.
