"""
DARS 2 — Mavzu 5: JSON bilan ishlash  ⭐ ENG MUHIM

JSON — ma'lumot almashish standarti. Backend'da API'lar aynan shu formatda
ma'lumot yuboradi/qabul qiladi. Python <-> JSON moslik:

    dict  <-> object  {}          list  <-> array  []
    str   <-> string              int/float <-> number
    True  <-> true                False <-> false        None <-> null

    json.dumps(obj)   -> obyektni JSON MATNGA (string)
    json.loads(matn)  -> JSON matndan Python obyektiga
    json.dump(obj, f) -> to'g'ridan-to'g'ri FAYLGA yozadi
    json.load(f)      -> FAYLdan o'qiydi
"""

import json

# --- 1. dumps / loads (matn bilan ishlash) ---
buyurtma = {"id": 1, "mijoz": "Ali", "summa": 75000, "yetkazildi": False}

# ensure_ascii=False -> lotin/kirill harflar o'qiladigan holda saqlanadi.
matn = json.dumps(buyurtma, ensure_ascii=False)
print(matn)          # {"id": 1, "mijoz": "Ali", "summa": 75000, "yetkazildi": false}
print(type(matn))    # <class 'str'>

qayta = json.loads(matn)
print(qayta["mijoz"])   # Ali
print(type(qayta))      # <class 'dict'>

# --- 2. Ro'yxatni JSON FAYLGA saqlash ---
buyurtmalar = [
    {"id": 1, "mijoz": "Ali", "summa": 75000},
    {"id": 2, "mijoz": "Vali", "summa": 42000},
]

with open("buyurtmalar.json", "w", encoding="utf-8") as f:
    # indent=2 -> chiroyli, o'qishga oson ko'rinish beradi.
    json.dump(buyurtmalar, f, ensure_ascii=False, indent=2)
print("Faylga saqlandi")

# --- 3. JSON fayldan qayta o'qish ---
with open("buyurtmalar.json", "r", encoding="utf-8") as f:
    yuklangan = json.load(f)

jami = sum(b["summa"] for b in yuklangan)
print(f"Jami {len(yuklangan)} ta buyurtma, umumiy summa: {jami} so'm")


# --- 4. ⭐ Custom OBYEKTNI (class) JSON'ga saqlash va qayta tiklash ---
# JSON faqat dict/list/str/number ni biladi. Shuning uchun obyektni avval
# dict'ga aylantiramiz (to_dict), keyin dict'dan qayta yaratamiz (from_dict).
class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

    def to_dict(self):
        """Obyekt -> dict (saqlash uchun)."""
        return {"nom": self.nom, "narx": self.narx}

    @classmethod
    def from_dict(cls, d):
        """dict -> Obyekt (qayta tiklash uchun)."""
        return cls(d["nom"], d["narx"])


m = Mahsulot("Olma", 12000)

# Saqlash:  obyekt -> dict -> JSON fayl
with open("mahsulot.json", "w", encoding="utf-8") as f:
    json.dump(m.to_dict(), f, ensure_ascii=False, indent=2)

# O'qish:   JSON fayl -> dict -> obyekt
with open("mahsulot.json", "r", encoding="utf-8") as f:
    m2 = Mahsulot.from_dict(json.load(f))

print(f"Qayta tiklandi: {m2.nom} — {m2.narx} so'm")
print(type(m2))   # <class '__main__.Mahsulot'>  -> yana to'liq obyekt!
