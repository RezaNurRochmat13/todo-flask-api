# 📝 Flask TODO API

Project REST API TODO List sederhana menggunakan:
- Flask + Flask-SQLAlchemy
- PostgreSQL (via Docker)
- Docker Compose

---

## 🚀 Fitur

- Tambah todo
- Tampilkan semua todo
- Toggle status selesai
- Hapus todo

---

## ⚙️ Requirements

- Python ≥ 3.7
- Docker + Docker Compose

---

## 📦 Instalasi

### 1. Clone repo
```bash
git clone https://github.com/username/python-flask-todo-api.git
cd python-flask-todo-api
```

### 2. Setup virtualenv
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database instance
```bash
cd infra/
docker-compose up
```

### 5. Run server
```bash
cd ../
python3 app.py
```

📁 Struktur Project
```bash
.
├── app.py
├── config.py
├── docker-compose.yml
├── models.py
├── requirements.txt
├── .gitignore
└── README.md
```
