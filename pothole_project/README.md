# Pothole Reporting Web Application

This is a minimal Django-based Pothole Reporting application (frontend: HTML/CSS/Vanilla JS; backend: Django + SQLite).

Quick setup (Windows PowerShell)

1. Create and activate virtual environment
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies
```powershell
pip install -r requirements.txt
```

3. Prepare project
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Create media folder and run server
```powershell
mkdir media
python manage.py runserver
```

App features
- Home page with intro and link to report form
- Report page with title, description, image upload, severity and map-based location picker (Leaflet via CDN)
- Dashboard listing reports with images, severity, status and location
- Admin panel to update status (Reported, In Progress, Fixed)

Notes
- Image uploads are saved to `media/pothole_images/` (development). Ensure `Pillow` is installed.
- Leaflet is loaded from a CDN in `templates/report_pothole.html`. The map captures latitude and longitude into hidden form fields.
- Static files are in `static/` (CSS and JS). Templates are in `templates/`.
- For production, set `DEBUG = False` in `pothole_project/settings.py`, set a secure `SECRET_KEY`, and configure static/media hosting.

Useful paths
- Project settings: `pothole_project/pothole_project/settings.py`
- App models/views: `pothole_project/reports/models.py`, `pothole_project/reports/views.py`
- Templates: `pothole_project/templates/`
- Static: `pothole_project/static/`

Next steps (suggested)
- Add `requirements-dev.txt` and tests.
- Add pagination and CSV export for the dashboard.
- Add email notifications for high-severity reports.
