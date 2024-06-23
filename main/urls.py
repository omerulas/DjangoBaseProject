from main import views

from django.urls import path

urlpatterns = [
    path(route='', view=views.Main.as_view(), name='main'),
]