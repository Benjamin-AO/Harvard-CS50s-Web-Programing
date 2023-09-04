from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    #path("<str:searched_page>", views.search, name="anything"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new_page", views.add_newPage, name="new_page"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("cancel_edit", views.cancel_edit, name="cancel_edit"),
    path("random_page", views.random_page, name="random_page"),
]
