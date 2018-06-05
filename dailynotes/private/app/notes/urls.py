from django.urls import path
from notes.views import *

urlpatterns = [
    path("", get_profile, name="main"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("profile/<int:user_id>/", profile_page, name="profile"),
    path("profile/<int:user_id>/settings/", change_password, name="settings"),
    path("note/new/", edit_note, name="note_create"),
    path("note/<int:note_id>/", read_note, name="note_read"),
    path("note/<int:note_id>/edit/", edit_note, name="note_edit")
]