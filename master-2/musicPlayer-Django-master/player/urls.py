from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('music/<id_music>', views.listen_music),

]