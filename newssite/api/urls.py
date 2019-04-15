from django.conf.urls import url
from django.urls import path
from newssite import views

urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('post', views.PostView.as_view({'get':'list'})),
    path('posts/<int:pk>', views.PostView.as_view({'get': 'retrieve'})),
    path('tag/list', views.TagView.list),
]