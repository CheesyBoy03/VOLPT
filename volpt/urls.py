from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('timetable/', include('timetable.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
