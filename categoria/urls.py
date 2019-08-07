from django.urls import path
from categoria.views import CategoryCreateView, CategoryUpdateView, CategoryListView, CategoryDeleteView         

app_name = 'categoria'

urlpatterns = [
    path('createcategory', CategoryCreateView.as_view(), name = 'createcategory'),    
    path('categoria/<int:pk>/alterar', CategoryUpdateView.as_view(), name = 'update_category'),
    path('showCategories',CategoryListView.as_view(), name='showCategories'),
    path('categoria/<int:pk>/deletar', CategoryDeleteView.as_view(), name = 'deleteCategories'),

]