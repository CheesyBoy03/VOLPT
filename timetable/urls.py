from django.urls import path
from .views import *

urlpatterns = [
    path('', timetable_view),
]
