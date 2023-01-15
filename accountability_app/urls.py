from django.urls import path

from . import views

app_name = "accountability_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("new_post/", views.new_post, name="new_post"),
]
