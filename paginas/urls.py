from django.urls import path
from paginas import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/",views.about,name='about'),
    path("projects/",views.projects,name='projects')
]