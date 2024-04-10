from django.urls import path
from .views import *

urlpatterns = [
    path('add/',add_album,name="add_album"),
    path('edit/<int:id>',edit_albm,name="edit_albm"),
    path('delete/<int:id>',delete_albm,name="delete_albm"),
]