from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, AboutPageView

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', AboutPageView.as_view(), name='about'),
]