# 🐍 DARS 2 — Example kodlar

OOP va ma'lumotni saqlash mavzulari bo'yicha **ishga tushiriladigan** namunalar.
Har bir fayl mustaqil — alohida ishlatish mumkin. Misollar do'kon/buyurtma
mavzusida (kurs kompaund loyihasi "Buyurtmalar tahlilchisi" bilan bog'liq).

## 📂 Fayllar

| # | Fayl | Mavzu |
|---|------|-------|
| 1 | [`01_class_obyekt.py`](01_class_obyekt.py) | Class, obyekt, `__init__`, `self`, attribute, method |
| 2 | [`02_inheritance.py`](02_inheritance.py) | Inheritance (meros olish), `super()`, `isinstance` |
| 3 | [`03_encapsulation.py`](03_encapsulation.py) | Encapsulation — `public` / `_protected` / `__private` |
| 4 | [`04_polymorphism.py`](04_polymorphism.py) | Polymorphism (ko'p shakllilik), duck typing |
| 5 | [`05_abstraction.py`](05_abstraction.py) | Abstraction — `abc`, `@abstractmethod` |
| 6 | [`06_str_repr.py`](06_str_repr.py) | Dunder metodlar — `__str__`, `__repr__`, `__eq__`, `__len__` |
| 7 | [`07_property.py`](07_property.py) | `@property` — getter / setter |
| 8 | [`08_classmethod_staticmethod.py`](08_classmethod_staticmethod.py) | `@classmethod` va `@staticmethod` |
| 9 | [`09_fayllar.py`](09_fayllar.py) | Fayl o'qish/yozish, `with` (context manager) |
| 10 | [`10_json.py`](10_json.py) | JSON `dump`/`load`, obyektni saqlash ⭐ **ENG MUHIM** |
| 11 | [`11_csv.py`](11_csv.py) | CSV bilan tanishish (`DictWriter` / `DictReader`) |

## ▶️ Ishga tushirish

```bash
cd examples
python 01_class_obyekt.py
# yoki istalgan boshqa fayl
```

> 9, 10, 11-fayllar ishga tushirilganda shu papkada natija fayllari
> (`mahsulotlar.txt`, `buyurtmalar.json`, `mahsulotlar.csv` va h.k.) yaratiladi.

## 🎯 O'rganish tartibi

1 → 2 → 3 → 4 → 5 (OOP asoslari va tamoyillari)
→ 6 → 7 → 8 (dunder va dekoratorlar)
→ 9 → 10 → 11 (fayl va ma'lumotni saqlash).

10-fayl (JSON) — darsning eng muhim qismi: OOP + fayl bilimini birlashtiradi.
