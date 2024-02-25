from django.urls import path

from .views import profile, delete_birthday_record_view, delete_account_view, landing_page

urlpatterns = [
    path("", landing_page, name="landing-page"),
    path("profile/", profile, name="profile"),
    path("delete-record/<int:pk>", delete_birthday_record_view, name="delete-record"),
    path("delete-account/", delete_account_view, name="delete-account"),
]
