"""
from django.urls import path
from newssite import views

urlpatterns = [
    path('post/list', views.PostView.list),
    path('category/list', views.CategoryView.list),
    path('tag/list', views.TagView.list),
]
"""