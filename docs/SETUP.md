# Setup Guide

## Initial Project Setup

### 1. Database Setup

#### PostgreSQL Setup

```bash
# Create database
createdb travello

# Create user (optional)
createuser travello_user
```

Or using psql:

```sql
CREATE DATABASE travello;
CREATE USER travello_user WITH PASSWORD 'your_password';
ALTER ROLE travello_user SET client_encoding TO 'utf8';
ALTER ROLE travello_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE travello_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE travello TO travello_user;
```

#### SQLite Setup (Development)

SQLite works out of the box. Just update `.env`:

```
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### 2. Virtual Environment

```bash
# Create
python -m venv .venv

# Activate
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

```bash
# Copy example
cp .env.example .env

# Edit with your settings
nano .env
```

Key settings:

```
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=your-very-secret-key-here
DB_NAME=travello
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User

```bash
python manage.py createsuperuser
```

You'll be prompted for:
- Username
- Email
- Password (twice)

### 7. Create Sample Data (Optional)

```bash
python manage.py shell

# In the Django shell:
from destination.models import Destination, Testimonial, HomeSlider

# Create destination
d = Destination.objects.create(
    name='Paris',
    price=500,
    description='City of lights and romance',
    offer=True
)
d.save()

# Create testimonial
t = Testimonial.objects.create(
    author='John Doe',
    position='CEO, TravelCo',
    content='Amazing service and destinations!'
)
t.save()

# Create slider
s = HomeSlider.objects.create(title='Summer Vacation')
s.save()

exit()
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Access at: `http://localhost:8000`
Admin at: `http://localhost:8000/admin`

## Production Setup

### 1. Environment Configuration

```bash
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=very-long-random-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_ENGINE=django.db.backends.postgresql
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 2. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 3. Run Migrations

```bash
python manage.py migrate --noinput
```

### 4. Deploy with Gunicorn

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn travello.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --worker-class sync \
    --timeout 120
```

### 5. Setup Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 6. Setup SSL/HTTPS

```bash
# Using Certbot
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com
```

### 7. Setup Systemd Service

Create `/etc/systemd/system/travello.service`:

```ini
[Unit]
Description=Travello Django Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/travello
ExecStart=/path/to/venv/bin/gunicorn \
    --workers 4 \
    --bind unix:/run/gunicorn.sock \
    travello.wsgi:application

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable travello
sudo systemctl start travello
```

## Docker Setup

### Build and Run

```bash
docker-compose up --build
```

Access at: `http://localhost`

### Create Admin User in Docker

```bash
docker-compose exec web python manage.py createsuperuser
```

### Run Migrations in Docker

```bash
docker-compose exec web python manage.py migrate
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>
```

### Permission Denied on Media/Static

```bash
chmod -R 755 media/
chmod -R 755 staticfiles/
```

### Database Connection Failed

```bash
# Test connection
psql -h localhost -U postgres -d travello
```

### Module Not Found

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

## Next Steps

1. Customize templates in `templates/`
2. Add your branding and images
3. Configure email settings
4. Setup Sentry for error tracking
5. Configure Redis for caching
6. Setup CI/CD pipeline

See [README.md](../README.md) for more information.

