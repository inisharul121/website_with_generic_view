from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index' ),
    path('<int:album_id>/',views.detail, name='detail' ),
]
