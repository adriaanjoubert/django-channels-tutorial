from django.urls import path

from file_download import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
