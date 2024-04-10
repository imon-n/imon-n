from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home, name="homepage"),
    path('aboutpage/',views.about, name="aboutpage"),
    path('formpage/',views.form, name="formpage"),
    path('dj_form/',views.dj_form, name ="dj_form")
]
