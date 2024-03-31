from django.urls import path
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BlogPostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]
