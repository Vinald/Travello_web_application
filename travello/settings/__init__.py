"""
Settings package initialization.
Imports the appropriate settings module based on the DJANGO_SETTINGS_MODULE environment variable.
"""

import os
from pathlib import Path

# Determine which settings module to use
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development').lower()

if ENVIRONMENT == 'production':
    from .production import *  # noqa
elif ENVIRONMENT == 'development':
    from .development import *  # noqa
else:
    from .development import *  # noqa

# Ensure BASE_DIR is available
if 'BASE_DIR' not in globals():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

