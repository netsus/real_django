from django.urls import path
from . import views

app_name="blog"

urlpatterns=[
    path("", views.post_list, name="post_list" ),
    path("<int:pk>", views.post, name="post" ),
    path("new/", views.post_create, name="post_create" ),
    path("<int:pk>/edit", views.post_edit, name="post_edit" ),
]