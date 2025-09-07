# 🎬 MovieHub

MovieHub is a Django-based web app to explore movies by genre, view details, and leave comments. Authenticated users can also add new movies.

---

## 🚀 Features
- Browse movies by genre
- View movie details: description, release date, genre
- Leave comments (login required)
- Add new movies (authenticated users)
- Responsive design with carousel for featured movies

---

## 🛠 Tech Stack
- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, MDB UI Kit  
- **Database:** SQLite / MySQL  

---

## ⚡ Installation
```bash
git clone https://github.com/yourusername/MovieHub.git
cd MovieHub
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
