from django.urls import path

from .views import (
    PostCreateAPIView,
    PostListAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDeliteAPIView,
)


urlpatterns = [
    path("post/create/", PostCreateAPIView.as_view(), name="post_create"),
    path("post/", PostListAPIView.as_view(), name="post_list"),
    path("post/get/<int:pk>/", PostRetrieveAPIView.as_view(), name="post_get"),
    path("post/update/<int:pk>/", PostUpdateAPIView.as_view(), name="post_update"),
    path("post/delete/<int:pk>/", PostDeliteAPIView.as_view(), name="post_delete"),
]
