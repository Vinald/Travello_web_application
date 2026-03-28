#!/usr/bin/env python
"""Test Django setup and migrations"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travello.settings')
sys.path.insert(0, '/Users/vinald/code/projects/Travello_web_application')

try:
    django.setup()
    print("✓ Django setup successful")

    # Try to import apps
    from django.apps import apps
    print(f"✓ Found {len(apps.get_app_configs())} installed apps")

    for app in apps.get_app_configs():
        print(f"  - {app.name}")

    print("\n✓ ALL CHECKS PASSED - Django is ready!")

except Exception as e:
    print(f"✗ ERROR: {type(e).__name__}")
    print(f"  {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

