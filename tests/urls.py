from django.urls import path
from social_connector.views import ig_token


urlpatterns = [
    path('ig_auth/', ig_token, name="ig_auth"),
]
