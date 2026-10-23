import os

BASE_URL = os.getenv("BASE_URL", "https://foodgram-frontend-1.foodgram.education-services.ru").rstrip("/")
SELENOID_URL = os.getenv("SELENOID_URL", "")
BROWSER_VERSION = os.getenv("BROWSER_VERSION", "")
TIMEOUT = 20
