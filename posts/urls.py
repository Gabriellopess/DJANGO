# This file means

from django.urls import path
from posts.views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('showPosts',PostListView.as_view(), name='showPosts'),
    path('createposts',PostCreateView.as_view(), name='createPosts_posts'),
    path('posts/<int:pk>/alterar', PostUpdateView.as_view(), name = 'update_post'),
    path('posts/<int:pk>/deletar', PostDeleteView.as_view(), name = 'delete_post'),
]