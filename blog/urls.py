from django.urls import path
from . import views

app_name="blog"

urlpatterns=[
    path("", views.post_list, name="post_list" ),
    path("<int:pk>", views.post, name="post" ),
    path("new/", views.post_create, name="post_create" ),
    path("<int:pk>/edit", views.post_edit, name="post_edit" ),
    path("<int:pk>/delete", views.post_delete, name="post_delete" ),
    path("<int:post_pk>/comments/new", views.comment_create, name="comment_create" ),
    path("<int:post_pk>/comments/<int:pk>/edit", views.comment_edit, name="comment_edit" ),
    path("<int:post_pk>/comments/<int:pk>/delete", views.comment_delete, name="comment_delete" ),
]