# 🐍 DARS 3 — Example kodlar (standart kutubxonalar)

Loyihada **eng ko'p ishlatiladigan** standart kutubxonalar bo'yicha
**ishga tushiriladigan** namunalar. Har bir fayl mustaqil ishlaydi.
Misollar do'kon/buyurtma mavzusida (kurs kompaund loyihasi
"Buyurtmalar tahlilchisi" bilan bog'liq).

## 📂 Fayllar

| # | Fayl | Kutubxona | Loyihada nega kerak |
|---|------|-----------|---------------------|
| 1 | [`01_os.py`](01_os.py) | `os` | Env o'qish, papka yaratish, yo'l birlashtirish |
| 2 | [`02_pathlib.py`](02_pathlib.py) | `pathlib` ⭐ | Fayl yo'llari bilan zamonaviy, xavfsiz ishlash |
| 3 | [`03_argparse.py`](03_argparse.py) | `argparse` | Terminaldan (CLI) argument qabul qilish |
| 4 | [`04_datetime.py`](04_datetime.py) | `datetime` | Hisobot sanasi, log vaqti, timestamp |
| 5 | [`05_random.py`](05_random.py) | `random` | Test (soxta) ma'lumot, tasodifiy tanlov |

## ▶️ Ishga tushirish

```bash
cd examples
python 01_os.py
# yoki istalgan boshqa fayl
```

`argparse` misolini argument bilan sinab ko'ring:

```bash
python 03_argparse.py buyurtmalar.json --oy yanvar --limit 3
python 03_argparse.py --help
```

> 1 va 2-fayllar ishga tushirilganda shu papkada `hisobotlar/` papkasi
> va namuna fayllar hosil bo'ladi (`.gitignore` ga qo'shsangiz bo'ladi).

## 🎯 O'rganish tartibi

1 → 2 (fayl yo'llari: `os` → zamonaviy `pathlib`)
→ 3 (`argparse` — dasturni tashqaridan sozlash)
→ 4 → 5 (`datetime` va `random` — sana/vaqt va tasodif).

> 💡 Bular Python bilan birga keladi — o'rnatish shart emas, faqat `import`.
> Tashqi paketlar (`requests`, `python-dotenv`) esa `uv add` / `pip install`
> bilan o'rnatiladi — buni **`qollanma.md`** dan ko'ring.
