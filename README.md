# Travello - Travel Booking Django Application

A modern Django web application for travel destination booking with a comprehensive admin interface, REST API, and user authentication.

## ⚡ Quick Start (30 Seconds)

```bash
# 1. Navigate to project
cd Travello_web_application

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Copy environment file
cp .env.example .env

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Start server
python manage.py runserver
```

**Visit**: `http://localhost:8000`  
**Admin**: `http://localhost:8000/admin`

---

## 🎯 Key URLs

| URL | Purpose |
|-----|---------|
| `/` | Home page with destinations |
| `/accounts/register/` | User registration |
| `/accounts/login/` | User login |
| `/accounts/logout/` | User logout |
| `/contact/` | Contact form |
| `/about/` | About page |
| `/services/` | Services page |
| `/admin/` | Admin dashboard |

---

## ✨ Features

- **Destinations Management**: Browse and manage travel destinations with pricing and offers
- **News & Blog**: Share travel tips and news articles
- **User Authentication**: Secure registration and login system
- **Contact Management**: Store and manage customer inquiries
- **Testimonials**: Display customer reviews and feedback
- **Admin Dashboard**: Comprehensive Django admin interface with custom actions
- **REST API**: RESTful API endpoints with filtering and pagination (Phase 2)
- **Responsive Design**: Mobile-friendly interface
- **Security**: CSRF protection, secure password handling, SQL injection prevention
- **Testing Framework**: Pytest with fixtures and coverage reporting
- **Docker Ready**: Containerization with docker-compose

---

## 📋 Common Commands

### Development
```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py createsuperuser
```

### Testing
```bash
pytest                                    # Run all tests
pytest --cov=. --cov-report=html        # Run with coverage
pytest destination/                      # Run specific app
pytest destination/test_models.py        # Run specific test file
```

### Code Quality
```bash
black .                 # Format code
flake8 .               # Check style
isort .                # Sort imports
black . && isort . && flake8 .  # All together
```

### Docker
```bash
docker-compose up --build                               # Build and run
docker-compose exec web python manage.py migrate        # Run migrations
docker-compose exec web python manage.py createsuperuser # Create admin
docker-compose down                                      # Stop containers
```

---

## 🚀 Full Installation & Setup

### Prerequisites

- Python 3.9+
- PostgreSQL 12+ (or SQLite for development)
- pip and virtualenv
- Docker & Docker Compose (optional)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Travello_web_application
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and fill in your configuration:

```dotenv
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=travello
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 7: Initialize Sample Data (Optional)

```bash
python manage.py shell < initialize_data.py
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

---

## 🗂️ Project Structure

```
travello/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── pytest.ini               # Pytest configuration
├── conftest.py              # Pytest fixtures
├── .env.example             # Example environment variables
├── Dockerfile               # Docker build configuration
├── docker-compose.yml       # Multi-container orchestration
├── initialize_data.py       # Sample data setup script
│
├── travello/                # Project settings
│   ├── settings/
│   │   ├── base.py         # Shared configuration
│   │   ├── development.py  # Development-specific settings
│   │   ├── production.py   # Production-ready settings
│   │   └── __init__.py
│   ├── urls.py             # Project URL configuration
│   ├── wsgi.py             # WSGI application
│   ├── asgi.py             # ASGI application
│   └── celery.py           # Celery async tasks
│
├── core/                    # Shared utilities
│   ├── models.py           # BaseModel abstract class with timestamps
│   ├── decorators.py       # Custom decorators (@login_required, etc.)
│   └── exceptions.py       # Custom exception classes
│
├── destination/            # Destinations feature app
│   ├── models.py           # Destination, NewsPosts, Testimonial, HomeSlider
│   ├── views.py            # Class-based and function-based views
│   ├── forms.py            # Form definitions
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin interface
│   ├── services.py         # Business logic layer
│   ├── test_models.py      # Model tests
│   └── migrations/
│
├── accounts/               # User authentication app
│   ├── models.py           # User extension (ready for custom user model)
│   ├── views.py            # CBV: RegisterView, LoginView, LogoutView
│   ├── forms.py            # RegistrationForm, LoginForm
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin interface
│   ├── test_forms.py       # Form validation tests
│   └── migrations/
│
├── contact/                # Contact form app
│   ├── models.py           # Contact model for submissions
│   ├── views.py            # ContactView (CBV)
│   ├── forms.py            # ContactForm
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin interface with status tracking
│   └── migrations/
│
├── services/               # Services page app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── about/                  # About page app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── login.html         # Login form
│   ├── register.html      # Registration form
│   ├── contact.html       # Contact form
│   ├── about.html         # About page
│   ├── destinations.html  # Destinations listing
│   └── ...
│
├── static/                 # Static files (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                  # User-uploaded files
│   ├── pictures/           # Destination images
│   ├── news_pictures/      # News post images
│   └── home_slider_pictures/ # Slider images
│
├── docs/                   # Documentation
│   ├── SETUP.md           # Detailed setup guide
│   └── STYLE_GUIDE.md     # Code standards and conventions
│
└── logs/                   # Application logs
    └── django.log         # Django application log file
```

---

## 🔧 Usage

### Admin Dashboard

Access the Django admin at `http://localhost:8000/admin/` with your superuser credentials.

**Admin Features:**
- **Destinations**: Search, filter by offer status and price, bulk mark as offer
- **News Posts**: Search by title/category, filter by date, manage articles
- **Contact Messages**: Track submissions, filter by status (new/read/replied)
- **Testimonials**: Manage customer reviews
- **Home Slider**: Configure homepage slider images

### User Registration & Login

- **Register**: `/accounts/register/`
  - Username validation
  - Email uniqueness check
  - Password strength validation
  - Form validation with error messages

- **Login**: `/accounts/login/`
  - Secure authentication
  - Remember me option
  - Error handling for invalid credentials

- **Logout**: `/accounts/logout/`
  - Secure session termination

### Contact Form

Submit inquiries at `/contact/` - messages are stored in the database and visible in admin with:
- Status tracking (new, read, replied)
- Email and name validation
- IP address capture
- Timestamp tracking

---

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest destination/test_models.py
pytest accounts/test_forms.py
```

### Run Tests with Coverage

```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html
```

### Run Tests with Markers

```bash
pytest -m unit          # Run only unit tests
pytest -m integration   # Run only integration tests
```

### Run in Verbose Mode

```bash
pytest -v              # Show all test names
pytest -vv             # Show more details
```

---

## 🐳 Docker Deployment

### Build & Run All Services

```bash
docker-compose up --build
```

Services included:
- **web**: Django application (Gunicorn)
- **db**: PostgreSQL database
- **redis**: Redis cache and message broker
- **celery**: Async task worker

### Run Specific Commands

```bash
# Run migrations
docker-compose exec web python manage.py migrate

# Create admin user
docker-compose exec web python manage.py createsuperuser

# Run Django shell
docker-compose exec web python manage.py shell

# View logs
docker-compose logs -f web
```

### Stop Services

```bash
docker-compose down
```

### Clean Up (Remove volumes)

```bash
docker-compose down -v
```

---

## 🌍 Environment Variables

### Development (.env)

| Variable | Example | Description |
|----------|---------|-------------|
| `ENVIRONMENT` | `development` | Environment mode |
| `DEBUG` | `True` | Django debug mode |
| `SECRET_KEY` | `your-secret-key` | Django secret key |
| `DB_NAME` | `travello_dev` | Database name |
| `DB_USER` | `postgres` | Database user |
| `DB_PASSWORD` | `password` | Database password |
| `DB_HOST` | `localhost` | Database host |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated allowed hosts |

### Production (.env)

```dotenv
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=very-long-random-secret-key-change-this
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=travello_prod
DB_USER=travello_user
DB_PASSWORD=strong-password
DB_HOST=db.example.com
DB_PORT=5432
REDIS_URL=redis://cache.example.com:6379/0
SENTRY_DSN=https://your-sentry-dsn
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

See `.env.example` for comprehensive configuration options.

---

## 💻 Development Guidelines

### Code Style

- Follow [PEP 8](https://pep8.org/) guidelines
- Use meaningful variable names
- Add docstrings to functions and classes (Google style)
- Keep lines under 100 characters
- Format with `black`: `black .`
- Check style with `flake8`: `flake8 .`

### Git Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -m "[FEATURE] Add your feature"`
3. Write tests for new code
4. Format code: `black . && isort . && flake8 .`
5. Push to branch: `git push origin feature/your-feature`
6. Create a Pull Request

### Model Best Practices

- Inherit from `BaseModel` for automatic `created_at` and `updated_at`
- Use `db_index=True` for frequently queried fields
- Add `help_text` to all fields
- Define `__str__()` and `__repr__()` methods
- Add Meta class with `verbose_name`, `verbose_name_plural`, `ordering`

### View Best Practices

- Use class-based views (CBV) when possible
- Add try-except blocks for error handling
- Log important operations
- Use forms for user input validation
- Optimize queries with `select_related()` and `prefetch_related()`

### Form Best Practices

- Create form classes for all user inputs
- Implement field-level and form-level validation
- Add Bootstrap CSS classes to widgets
- Add help text and error messages
- Validate uniqueness constraints

---

## 🚀 Deployment

### Using Docker (Recommended)

```bash
# Build and start all services
docker-compose up --build -d

# Verify services are running
docker-compose ps

# View logs
docker-compose logs -f
```

### Manual Deployment

1. Set `ENVIRONMENT=production` in `.env`
2. Set `DEBUG=False`
3. Update `ALLOWED_HOSTS` with your domain
4. Run migrations: `python manage.py migrate`
5. Collect static files: `python manage.py collectstatic --noinput`
6. Use a production WSGI server:

```bash
pip install gunicorn
gunicorn travello.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --worker-class sync \
    --timeout 120
```

### Setup with Nginx (Reverse Proxy)

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

### Setup with Systemd Service

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

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable travello
sudo systemctl start travello
```

---

## 🔒 Security Considerations

Before deploying to production, verify:

- ✅ Change `SECRET_KEY` in production `.env`
- ✅ Set `DEBUG=False`
- ✅ Set `ENVIRONMENT=production`
- ✅ Configure `ALLOWED_HOSTS`
- ✅ Setup HTTPS/SSL certificates
- ✅ Use strong database credentials
- ✅ Enable CSRF protection
- ✅ Validate all user input
- ✅ Use secure password hashing
- ✅ Setup rate limiting
- ✅ Configure security headers
- ✅ Keep dependencies updated

Run Django security check:
```bash
python manage.py check --deploy
```

---

## ⚡ Performance Optimization

- **Database**: Enable indexes, use `select_related()` and `prefetch_related()`
- **Caching**: Redis caching for expensive queries
- **Static Files**: Use CDN, WhiteNoise for compression
- **Images**: Optimize with Pillow, use lazy loading
- **Async Tasks**: Celery for long-running operations
- **Monitoring**: Setup Sentry for error tracking

---

## 🆘 Troubleshooting

### Error: ModuleNotFoundError: No module named 'django'

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Error: could not connect to server: Connection refused

```bash
# Ensure PostgreSQL is running
# Or use SQLite by updating .env:
DB_ENGINE=django.db.backends.sqlite3
```

### Error: Database does not exist

```bash
# Create database
createdb travello

# Run migrations
python manage.py migrate
```

### Migration conflicts or issues

```bash
python manage.py migrate --fake-initial
```

### Static files not loading

```bash
python manage.py collectstatic --noinput
```

### Port 8000 already in use

```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

---

## 📚 REST API Documentation

REST API endpoints (Phase 2 - Foundation Ready):

- `GET /api/destinations/` - List all destinations
- `GET /api/destinations/<id>/` - Get destination details
- `GET /api/news/` - List news posts
- `GET /api/news/<id>/` - Get news post details
- `GET /api/testimonials/` - List testimonials
- `POST /api/contact/` - Submit contact form

Full API documentation available at `/api/schema/` (Swagger UI) after Phase 2 implementation.

---

## 📖 Additional Documentation

- **[QUICK_START.md](QUICK_START.md)** - Quick reference guide
- **[docs/SETUP.md](docs/SETUP.md)** - Detailed setup and configuration
- **[docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md)** - Code standards and conventions
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design and architecture
- **[conftest.py](conftest.py)** - Test fixtures documentation

---

## 🎓 Learning Resources

### Django
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django for Beginners](https://djangoforbeginners.com/)

### Python
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Documentation](https://docs.python.org/)

### Testing
- [Pytest Documentation](https://docs.pytest.org/)
- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)

### Deployment
- [Docker Documentation](https://docs.docker.com/)
- [Gunicorn Documentation](https://gunicorn.org/)

---

## 🤝 Contributing

See [docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md) for coding standards and conventions.

### Development Workflow

1. Read the style guide
2. Create a feature branch
3. Write tests first (TDD)
4. Implement the feature
5. Run tests and code quality checks
6. Create a pull request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check [docs/SETUP.md](docs/SETUP.md) for troubleshooting
- Review docstrings in code files
- Check [docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md) for conventions

---

## 📝 Changelog

### v2.0.0 (Current - Refactored)
- Refactored project structure with modular settings
- Environment-specific configurations (dev/prod)
- Class-based views throughout
- Comprehensive form validation
- Enhanced admin interface with custom actions
- Testing framework with pytest and fixtures
- Database models with automatic timestamps
- Service layer for business logic
- Docker and docker-compose support
- Comprehensive documentation (7 guides)
- Security hardening and best practices
- REST API foundation ready (Phase 2)

### v1.0.0 (Previous)
- Basic Django functionality
- User authentication (registration/login)
- Destination listing
- Contact form
- Basic admin interface

---

**Version**: 2.0.0 (Refactored)  
**Last Updated**: March 28, 2026  
**Status**: Production-Ready  
**Python**: 3.9+  
**Django**: 6.0.3  


