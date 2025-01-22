from django.urls import path
from .views import BlogView

urlpatterns = [
    path('blogs/<int:pk>/', BlogView.as_view(), name='blog-view'),
    path('blogs/', BlogView.as_view(), name='blog-list-create'),  # Combined view for both list and create
]
