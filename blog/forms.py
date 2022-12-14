from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=[
            "title",
            "content",
            "tag_set",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= [
            "content",
        ]
        widgets = {
            "content": forms.Textarea(attrs={"rows":3})
        }
