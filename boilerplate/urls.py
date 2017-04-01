from django.conf import settings
from django.conf.urls import url

from .views import (
    HomeView,
)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]

if settings.DEBUG:
    # Serve static files in development - in production this is handled by whitenoise
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
