from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model() # 첫 번째 방법
# from accounts.models import User # 두 번째 방법

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User