from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.get_page, name="page_entry"),
    path("new_page", views.new_page, name="new_page")
]
