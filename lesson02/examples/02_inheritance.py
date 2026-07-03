"""
DARS 2 — Mavzu 2.1: Inheritance (meros olish)

Bir class boshqa classdan meros oladi: umumiy kod bir marta yoziladi,
keyin qayta ishlatiladi. "is-a" munosabati: Admin — bu Foydalanuvchi.
"""


# --- Ota (bazaviy) class ---
class Foydalanuvchi:
    def __init__(self, ism, email):
        self.ism = ism
        self.email = email

    def tanishtir(self):
        return f"{self.ism} ({self.email})"


# --- Bola class: Foydalanuvchi'dan meros oladi ---
class Admin(Foydalanuvchi):
    def __init__(self, ism, email, daraja):
        # super() — ota classning __init__ ini chaqiradi (kodni takrorlamaymiz).
        super().__init__(ism, email)
        self.daraja = daraja   # qo'shimcha, faqat Admin'ga xos attribute

    # Yangi method — faqat Admin'da bor.
    def bloklash(self, kim):
        return f"{self.ism} {kim}ni blokladi"


class Mijoz(Foydalanuvchi):
    def __init__(self, ism, email, balans=0):
        super().__init__(ism, email)
        self.balans = balans


admin = Admin("Ali", "ali@shop.uz", "super")
mijoz = Mijoz("Vali", "vali@mail.uz", 50000)

# Meros olingan method — ikkalasida ham ishlaydi.
print(admin.tanishtir())   # Ali (ali@shop.uz)
print(mijoz.tanishtir())   # Vali (vali@mail.uz)

# Faqat Admin'ga tegishli method.
print(admin.bloklash("spam-bot"))

# isinstance — obyekt qaysi classdan ekanini tekshiradi.
print(isinstance(admin, Admin))          # True
print(isinstance(admin, Foydalanuvchi))  # True  (meros tufayli)
print(isinstance(mijoz, Admin))          # False
