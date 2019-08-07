from django.urls import path
from comentarios.views import ComentariosListView, ComentariosCreateView, ComentariosUpdateView, ComentariosDeleteView

app_name = 'comentarios'

urlpatterns = [
    path('showComentarios',ComentariosListView.as_view(), name='showComentarios'),
    path('createcomentarios',ComentariosCreateView.as_view(), name='createComentarios'),
    path('comentarios/<int:pk>/alterar', ComentariosUpdateView.as_view(), name = 'update_comentarios'),
    path('comentarios/<int:pk>/deletar',ComentariosDeleteView.as_view(), name = 'delete_comentarios'),
]