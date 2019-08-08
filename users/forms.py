from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserSignupForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email']