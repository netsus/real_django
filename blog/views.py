from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from blog.models import Post


class Blog(ListView):
    model = Post

post_list = Blog.as_view()
class Post(LoginRequiredMixin, DetailView):
    model = Post

post = Post.as_view()
