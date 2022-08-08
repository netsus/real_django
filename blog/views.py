from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import PostForm
from blog.models import Post


class BlogListView(ListView):
    """Blog List View"""
    model = Post
    paginate_by = 4

post_list = BlogListView.as_view()


class PostDetailView(LoginRequiredMixin, DetailView):
    """Post Detail View"""
    model = Post

post = PostDetailView.as_view()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/blog_form.html"
    success_url = "/blog/"

post_create = PostCreateView.as_view()

