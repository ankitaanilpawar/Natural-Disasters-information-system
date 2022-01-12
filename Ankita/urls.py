from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Naturaldisaster.urls')),
    path('admin/', admin.site.urls),
    path('Earthquake/', include('Earthquake.urls')),
    path('Tornado/', include('Tornado.urls')),
    path('Tsunami/', include('Tsunami.urls')),
    path('Volcano/', include('Volcano.urls')),
    path('Donate/', include('Donate.urls'))
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
