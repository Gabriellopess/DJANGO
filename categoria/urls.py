from django.urls import path
from categoria.views import CategoryCreateView           #PostListView

app_name = 'categoria'

urlpatterns = [
    path('createcategory', CategoryCreateView.as_view(), name = 'createcategory'),    
    
    
    
    #path('showPosts',PostListView.as_view(), name='showPosts'),
    #path('posts/<int:pk>/deletar', PostDeleteView.as_view(), name = 'delete_post'),
]