import os

SECRET_KEY = "TESTONLY"

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = ["social_connector"]

ROOT_URLCONF = "tests.urls"

INSTAGRAM_APP_ID = os.environ.get("INSTAGRAM_APP_ID")
INSTAGRAM_SECRET = os.environ.get("INSTAGRAM_SECRET")
