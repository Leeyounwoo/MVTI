from django.urls import path
from . import views


app_name = 'recruits'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:recruit_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:recruit_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
