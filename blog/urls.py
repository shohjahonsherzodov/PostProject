from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, AboutPageView
from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
]