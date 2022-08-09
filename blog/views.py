from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    """Blog List View"""
    model = Post
    paginate_by = 4

post_list = PostListView.as_view()


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

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/blog_form.html"

    def test_func(self):
        return self.request.user == self.get_object().author



post_edit = PostUpdateView.as_view()
