from . import views
from django.urls import path
app_name='music'

urlpatterns = [
    #/music/
    path('',views.IndexView.as_view(), name='index' ),
    #/music/<album_id>
    path('<int:pk>/',views.DetailView.as_view(), name='detail' ),
    #/music/album/add/
    path('album/add/',views.CreateAlbum.as_view(), name='album-add' ),
    #/music/album/2/
    path('album/<int:pk>/',views.UpdateView.as_view(), name='album-update' ),
    #/music/album/2/delete
    path('album/<int:pk>/delete/',views.DetailView.as_view(), name='album-delete' ),
    #/music/<album_id>/favorite
    path('<int:album_id>/favorite/',views.favorite, name='favorite' ),

]
