"""
DARS 2 — Mavzu 2.2: Encapsulation (inkapsulyatsiya / ma'lumotni yashirish)

Obyekt ichidagi ma'lumotni tashqaridan to'g'ridan-to'g'ri buzishdan himoya qilamiz.
Nomlash konventsiyasi:
    nom      -> public   (ochiq, erkin ishlatiladi)
    _nom     -> protected (ichki; "tegmang" degan ogohlantirish)
    __nom    -> private  (name mangling bilan yashiriladi)
"""
# setter, getter

class BankHisob:
    def __init__(self, egasi, boshlangich=0):
        self.egasi = egasi            # public
        self.__balans = boshlangich   # private — tashqaridan ko'rinmaydi

    def hisobga_qoshish(self, summa):
        if summa <= 0:
            print("Xato: summa musbat bo'lishi kerak")
            return
        self.__balans += summa

    def yechish(self, summa):
        if summa > self.__balans:
            print("Xato: mablag' yetarli emas")
            return
        self.__balans -= summa

    @property
    def balans(self):
        return self.__balans

    @balans.setter
    def balans(self, amount):
        self.__balans = amount


hisob = BankHisob("Ali", 100000)

hisob.hisobga_qoshish(50000)
hisob.yechish(30000)

# getter
print(hisob.balans)   # 120000
# setter
hisob.balans = 123012

# To'g'ridan-to'g'ri o'qib/o'zgartirib bo'lmaydi (himoyalangan):
# print(hisob.__balans)     # AttributeError!

# Faqat nazorat qilingan method orqali ishlaydi -> validatsiya kafolatlanadi:
hisob.yechish(999999)       # Xato: mablag' yetarli emas
hisob.hisobga_qoshish(-10)  # Xato: summa musbat bo'lishi kerak
print(hisob.balans)       # 120000  (qiymat saqlanib qoldi -> himoya ishladi)
