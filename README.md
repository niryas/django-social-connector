# django-social-connector

A sample Django app for OAuth Token Exchange to support Instagram Basic Display API.

> [!CAUTION] 
> **This app is not meant for production.** It lacks certain security features and certain customization options 
> which must be implemented based on the exact use case. It will **only work in `DEBUG` mode**, for development.

Use this app for **development only** and as a guide for adding your own token exchange backend endpoint.

## Adding to Django:
1. Install from PyPi:
`pip install django-social-connector`

2. Add to INSTALLED_APPS:
```py
# settings.py
INSTALLED_APPS = [
    # ...
    "social_connector",
    # ...
]
```

3. Add `INSTAGRAM_APP_ID` and `INSTAGRAM_SECRET` settings:
```py
# settings.py
import os

INSTAGRAM_APP_ID = os.environ.get("INSTAGRAM_APP_ID")
INSTAGRAM_SECRET = os.environ.get("INSTAGRAM_SECRET")
```
Note: Your `INSTAGRAM_SECRET` should be loaded and stored as a **secret key**. How to do that properly is outside the scope
of this guide and depends on your environment.

4. Add a token endpoint to your URLs:
```py
# urls.py
from django.urls import path
from social_connector.views import ig_token

urlpatterns = [
    # ...
    path('ig_token/', ig_token, name="ig_token"),
    # ...
]
```
You can customize the path and the name as needed.

5. The endpoint is ready for use in development. 

## Troubleshooting
### CORS Settings
Make sure your frontend host is allowed for CORS requests in Django.

## Moving to Production
***This app is for demonstration and development use only.***

For production, create your own view in your own codebase.

For being Production ready, the endpoint should have at least the following additional safeguards:
* CSRF protection
* Throttling (limited amount of requests per user per time)
* Further input checks and sanitation before sending the API request to Instagram
* Might require the user being logged in, depending on the specific app's use case

Adding these features will bloat this minimal sample, especially when trying to reduce requirements.
Implementation of some of these features also depend on your specific use case.

