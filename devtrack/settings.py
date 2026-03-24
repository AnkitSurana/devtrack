"""
Django settings for devtrack project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-k$!-@q0#!v-4w$hv*nb*pnm$i3s6%^%@w+-9&etzg(ui7u!+qj"
DEBUG = True
ALLOWED_HOSTS = ['*']

# We only need our custom app to load its URLs and Views
INSTALLED_APPS = [
    "issues",
]

# We stripped out sessions, auth, and messages middleware since this is a pure JSON API
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "devtrack.urls"
