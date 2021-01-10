from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.get_page, name="page_entry"),
    path("new_page", views.new_page, name="new_page"),
    path("edit_page/<str:entry>", views.edit_page, name="edit_page"),
    path("random_page", views.random_page, name="random_page")
]