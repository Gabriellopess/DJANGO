from django.urls import path
from users.views import UserListView

app_name = 'users'

urlpatterns = [
    path('list',UserListView.as_view(), name='list_users'),
]