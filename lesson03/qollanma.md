# 🛠 DARS 3 — Qo'llanma: Modul → Muhit → Git → GitHub

Bu — darsning **terminal (buyruqlar)** qismi. Python kodi bilan ko'rsatib
bo'lmaydigan mavzular shu yerda: virtual muhit, paketlar, Git va GitHub.

Ishga tushiriladigan Python namunalari esa: **[`examples/`](examples/)**

---

## 📦 1. Modul va paket — nega kerak?

Bitta ulkan `main.py` yozish o'rniga, kodni **modullarga** (fayllarga) va
**paketlarga** (papkalarga) bo'lamiz. Sabab:

- **Tartib** — har bir fayl bitta vazifa (mahsulot, hisobot, ...).
- **Qayta ishlatish** — bir marta yozib, ko'p joyda `import` qilamiz.
- **Jamoa** — har kim o'z faylida ishlaydi, to'qnashuv kamayadi.

| Tushuncha | Nima | Misol |
|-----------|------|-------|
| **Modul** | bitta `.py` fayl | `narx_util.py` |
| **Paket** | `__init__.py` bo'lgan papka | `dokon/` |
| **Submodul** | paket ichidagi modul | `dokon/mahsulot.py` |

> **Bog'lanish:** `import os`, `import datetime`, `from pathlib import Path` —
> bular ham modul! Farqi shundaki, ular Python bilan birga keladi (standart
> kutubxona) — ishga tushadigan namunalar: [`examples/`](examples/).
> `python-dotenv` esa tashqaridan `pip` bilan o'rnatiladi (keyingi bo'lim).

---

## 📌 2. Virtual muhit (`venv`) — nega kerak?

Har bir loyihaning **o'z paketlari** bo'ladi. A-loyiha `django==5.0`,
B-loyiha `django==4.2` talab qilishi mumkin. Agar hammasini bitta joyga
o'rnatsak — to'qnashuv. **Virtual muhit** — bu loyiha uchun alohida,
izolyatsiya qilingan Python "qutisi".

```bash
# 1. Muhit yaratish (.venv nomli papka paydo bo'ladi)
python -m venv .venv

# 2. Muhitni FAOLLASHTIRISH
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows (PowerShell)

# Faollashsa, terminalda (.venv) ko'rinadi:
#   (.venv) $

# 3. Chiqish
deactivate
```

> ⚠️ `.venv/` papkasini **hech qachon** GitHub'ga yubormaymiz —
> u `.gitignore` ichida bo'ladi (pastda).

---

## ⚡ 3. `uv` — zamonaviy va tez usul

`uv` — paket va muhitni bitta tez vositada boshqaradi (venv + pip o'rnini bosadi).

```bash
# Yangi loyiha yaratish (pyproject.toml avtomatik hosil bo'ladi)
uv init dokon-loyiha
cd dokon-loyiha

# Paket qo'shish (muhit avtomatik yaratiladi va yangilanadi)
uv add requests
uv add python-dotenv

# Kod ishga tushirish (muhitni o'zi faollashtiradi)
uv run main.py

# O'rnatilgan paketlarni sinxronlash (boshqa kompyuterda)
uv sync
```

`uv` barcha paketlarni `pyproject.toml` + `uv.lock` da yozib boradi —
qo'lda `requirements.txt` yozish shart emas.

---

## 📥 4. `pip` va `requirements.txt` (klassik usul)

`pip` — Python paket menejeri. Muhit faollashgan holatda ishlatiladi.

```bash
# Paket o'rnatish
pip install requests python-dotenv

# O'rnatilganlarni ro'yxatga yozish (dependency ro'yxati)
pip freeze > requirements.txt

# Boshqa kompyuterda o'sha ro'yxatdan o'rnatish
pip install -r requirements.txt
```

**`requirements.txt`** namunasi:

```
requests==2.32.3
python-dotenv==1.0.1
```

**`pyproject.toml`** — zamonaviy loyiha "pasporti" (metadata + dependency):

```toml
[project]
name = "dokon-loyiha"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.32",
    "python-dotenv>=1.0",
]
```

| | `requirements.txt` | `pyproject.toml` |
|---|---|---|
| Uslub | eski, oddiy | zamonaviy, standart |
| Ichida | faqat paketlar | metadata + paketlar + sozlama |
| Kim ishlatadi | `pip` | `uv`, `pip`, `poetry` |

---

## 🔐 5. Konfiguratsiya va maxfiylik (`.env`)

Token/parol kabi maxfiy ma'lumot **kodda emas**, `.env` faylida bo'ladi.
Koddan `os.getenv(...)` orqali o'qiladi (namuna: [`examples/01_os.py`](examples/01_os.py)).

`.env` fayli:

```
BOT_TOKEN=123456:AbCdEf...
DATABASE_URL=postgresql://user:parol@localhost:5432/dokon
```

Koddan o'qish:

```python
import os
from dotenv import load_dotenv

load_dotenv()                       # .env ni yuklaydi
token = os.getenv("BOT_TOKEN")      # o'qiydi
```

---

## 🙈 6. `.gitignore` — nimani yubormaslik ⭐ ENG MUHIM

`.gitignore` — Git'ga "bu fayllarni **kuzatma**" deb aytadigan ro'yxat.
Maxfiy va keraksiz fayllar GitHub'ga chiqmasligi uchun.

```gitignore
.env                # ⭐ maxfiy — HECH QACHON yubormaymiz
__pycache__/        # Python keshi
.venv/              # virtual muhit
.DS_Store           # macOS xizmat fayli
*.log
```

> 💡 Qoida: agar fayl **maxfiy** yoki **avtomatik hosil bo'ladigan** bo'lsa —
> `.gitignore` ga qo'shing. `.env.example` esa qo'shilmaydi (u namuna, maxfiy emas).

---

## 🐙 7. Git asoslari

Git — kodning **versiyalarini** saqlaydigan tizim (har bir o'zgarishni eslab qoladi).

```bash
# --- Bir marta sozlash (ismingiz) ---
git config --global user.name "Ismingiz"
git config --global user.email "email@example.com"

# --- Loyihada boshlash ---
git init                 # papkani git repozitoriyaga aylantiradi
git status               # holatni ko'rish (qaysi fayl o'zgardi)

# --- O'zgarishni saqlash (3 qadam) ---
git add .                # barcha o'zgarishni "sahna"ga qo'yish
git add examples/01_modul.py   # yoki bitta faylni
git commit -m "lesson03: modul va paket qo'shildi"

# --- Tarix ---
git log --oneline        # commitlar ro'yxati (qisqa)
```

**Git oqimi (workflow):**

```
  o'zgartirish  →  git add  →  git commit  →  (GitHub'ga) git push
   (ish maydoni)    (staging)    (tarix)          (bulut)
```

### Branch (shox) va merge

Branch — asosiy koddan ajralib, xavfsiz alohida ishlash uchun.

```bash
git branch                       # branchlar ro'yxati
git checkout -b feature/hisobot  # yangi branch yaratib, unga o'tish
# ... kod yozamiz, commit qilamiz ...

git checkout main                # asosiy branchga qaytish
git merge feature/hisobot        # ishni asosiyga qo'shish (birlashtirish)
```

---

## ☁️ 8. GitHub va portfolio

GitHub — Git repozitoriyalarni **onlayn** saqlaydigan joy (portfolio shu yerda).

```bash
# --- Lokal loyihani GitHub'ga bog'lash ---
git remote add origin https://github.com/foydalanuvchi/dokon-loyiha.git
git push -u origin main          # birinchi marta yuklash

# --- Keyingi safar ---
git push                         # o'zgarishlarni yuborish
git pull                         # GitHub'dan yangilikni olish

# --- Tayyor loyihani ko'chirib olish ---
git clone https://github.com/foydalanuvchi/dokon-loyiha.git
```

### Pull Request (PR)

PR — "mening branchimdagi ishni asosiy loyihaga qo'shing" degan **rasmiy so'rov**.
Jamoada kod aynan PR orqali ko'rib chiqiladi (review) va qo'shiladi.

**Oqim:**

```
  branch yaratish → commit → git push origin branch
       → GitHub'da "Compare & pull request" bosish
       → tavsif yozish → Reviewer tekshiradi → Merge
```

---

## 📝 9. README.md va Markdown

Har bir loyiha **README.md** bilan boshlanadi — bu loyihaning "yuzi".
Markdown — oddiy matnni chiroyli formatlaydigan yozuv tili.

```markdown
# Sarlavha (h1)
## Kichik sarlavha (h2)

**qalin**, *qiya*, `kod`

- ro'yxat elementi
- yana biri

1. raqamli
2. ro'yxat

[havola matni](https://example.com)

​```python
print("kod bloki")
​```
```

**Yaxshi README tarkibi:** loyiha nomi va tavsifi → o'rnatish (`install`) →
ishga tushirish (`run`) → misol → mualliflik.

---

## ✅ 10. Amaliy topshiriq (uy vazifa)

Kompaund loyiha ("Buyurtmalar tahlilchisi") ni professional ko'rinishga keltiring:

1. Kodni modullarga bo'ling: `mahsulot.py`, `hisobot.py` — `dokon/` paketiga.
2. `python -m venv .venv` bilan muhit yarating va faollashtiring.
3. `pip install python-dotenv`, so'ng `pip freeze > requirements.txt`.
4. `.env` (maxfiy) va `.env.example` (namuna) yarating.
5. `.gitignore` yozing (`.env`, `.venv/`, `__pycache__/` ...).
6. `git init` → `add` → `commit`.
7. GitHub'da repozitoriya oching, `push` qiling.
8. Chiroyli `README.md` yozing.
9. Yangi branch → kichik o'zgarish → **Pull Request** oching.

🎯 Natija: bu sizning **birinchi portfolio loyihangiz** bo'ladi.

---

> Keyingi qadam: **Backend Development** — HTTP, Telegram bot, SQL,
> PostgreSQL, SQLAlchemy, FastAPI, Django, DRF, Docker, Redis, Celery.
