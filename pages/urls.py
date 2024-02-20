from django.urls import path

from .views import list_create_birthday_records_view, delete_birthday_record_view

urlpatterns = [
    path("", list_create_birthday_records_view, name="home"),
    path("delete-record/<int:pk>", delete_birthday_record_view, name="delete-record"),
]
