from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/filter/<str:topic>/', views.filter_by_topic, name='filter_by_topic'),
    path('articles/<int:article_id>/comment/', views.add_comment, name='add_comment'),
]
