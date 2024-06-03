from django.urls import path
from .views import *




urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post-list'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post_create/', PostCreateView.as_view(), name='post-create'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post_delete/<int:pk>/', DeletePostView.as_view(), name='post-delete'),
    path('post_review/<int:pk>/', AddReview.as_view(), name='add-review'),
    path('review_update/<int:pk>/', ReviewUpdate.as_view(), name='review-update'),
    path('review_confirm_delete/<int:pk>/', ReviewDelete.as_view(), name='review-delete'),
]