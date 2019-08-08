from django.urls import path
from users.views import UserListView, UserLoginView, UserLogoutView, UserSignupView, UserDetailView

app_name = 'users'

urlpatterns = [
    path('list',UserListView.as_view(), name='list_users'),
    path('login', UserLoginView.as_view(), name = 'login_user'),
    path('logout', UserLogoutView.as_view(), name = 'logout_user'),
    path('signup', UserSignupView.as_view(), name = 'signup_user'),
    path('about/<int:pk>/user', UserDetailView.as_view(), name = 'about_user'),
]