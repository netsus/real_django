from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import resolve_url, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment


class PostListView(ListView):
    """Blog List View"""
    model = Post
    paginate_by = 4

post_list = PostListView.as_view()


class PostDetailView(LoginRequiredMixin, DetailView):
    """Post Detail View"""
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["comment_form"] = CommentForm()
        return context_data

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

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        return self.request.user == self.get_object().author

post_delete = PostDeleteView.as_view()

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return resolve_url("blog:post", self.kwargs["post_pk"])



comment_create = CommentCreateView.as_view()

class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/blog_form.html"

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return resolve_url("blog:post", self.kwargs["post_pk"])

comment_edit = CommentUpdateView.as_view()

class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return resolve_url("blog:post", self.kwargs["post_pk"])

comment_delete = CommentDeleteView.as_view()
