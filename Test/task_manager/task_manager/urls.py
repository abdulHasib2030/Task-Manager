from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import MainHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainHome, name='main-home'),
    path('', include('account.urls')),
    path('task/', include('tasks.urls')),
    ##### Api url ######
    path('api/', include('api.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
