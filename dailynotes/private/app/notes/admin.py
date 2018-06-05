from django.contrib import admin
from notes.models import Note


@admin.register(Note)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created"]
