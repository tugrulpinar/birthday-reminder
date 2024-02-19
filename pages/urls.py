from django.urls import path

from .views import birth_day_records_view

urlpatterns = [
    path("", birth_day_records_view, name="home"),
]
