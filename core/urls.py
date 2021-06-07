from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home

app_name = 'core'

urlpatterns = [
    path('', home, name='home')
    # path('', ib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)