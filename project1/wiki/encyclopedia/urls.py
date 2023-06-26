from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.newPage, name="newPage" ),
    path("edit/", views.editPage, name="editPage"),
    path("save/", views.savePage, name="savePage"),
    path("random/",views.rand, name="rand")
]
