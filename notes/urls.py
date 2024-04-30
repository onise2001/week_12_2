from django.urls import path
from .views import index, add_note, delete_note, show_note

urlpatterns = [
    path("", index),
    path("add_note/", add_note),
    path("delete_note/<str:id>", delete_note),
    path("note/<str:id>", show_note),
    
]
