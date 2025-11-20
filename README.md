Handmade Flowers Django Project (final)
--------------------------------------
- Unzip and open the folder.
- Create virtualenv & install dependencies:
    python -m venv venv
    source venv/bin/activate   # Windows: venv\Scripts\activate
    pip install -r requirements.txt
- Apply migrations:
    python manage.py migrate
- Create superuser:
    python manage.py createsuperuser
- Run development server:
    python manage.py runserver
- Admin available at /admin/
- Media files uploaded to media/ during development.
