#!/bin/bash
# Django Travello - Setup Commands
# Run these commands in order to get your project up and running

echo "🚀 Django Travello Project - Setup Script"
echo "=========================================="
echo ""

# Step 1: Install dependencies
echo "📦 Step 1: Installing dependencies..."
echo "Command: pip install -r requirements.txt"
echo ""
echo "Run this command:"
echo "  pip install -r requirements.txt"
echo ""

# Step 2: Create database
echo "🗄️  Step 2: Creating database..."
echo "Command: python manage.py migrate"
echo ""
echo "Run this command:"
echo "  python manage.py migrate"
echo ""

# Step 3: Create admin user
echo "👤 Step 3: Creating admin user..."
echo "Command: python manage.py createsuperuser"
echo ""
echo "Run this command:"
echo "  python manage.py createsuperuser"
echo ""
echo "You will be prompted to enter:"
echo "  - Username"
echo "  - Email"
echo "  - Password (enter twice)"
echo ""

# Step 4: Start development server
echo "🌐 Step 4: Starting development server..."
echo "Command: python manage.py runserver"
echo ""
echo "Run this command:"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  - Frontend: http://localhost:8000"
echo "  - Admin: http://localhost:8000/admin"
echo ""

# Additional useful commands
echo "📝 Additional Useful Commands:"
echo ""
echo "System check:"
echo "  python manage.py check"
echo ""
echo "Run tests:"
echo "  pytest"
echo ""
echo "Format code:"
echo "  black ."
echo ""
echo "Check code quality:"
echo "  flake8 ."
echo ""
echo "Django shell:"
echo "  python manage.py shell"
echo ""

echo "✅ Setup guide complete!"
echo "=========================================="

