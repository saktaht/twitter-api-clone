from django.urls import path

from .views import (
    PostCreateAndListAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
)


urlpatterns = [
    path("post/", PostCreateAndListAPIView.as_view(), name="post_list"),
    path("post/get/<int:pk>/", PostRetrieveAPIView.as_view(), name="post_get"),
    path("post/update/<int:pk>/", PostUpdateAPIView.as_view(), name="post_update"),
    path("post/delete/<int:pk>/", PostDeleteAPIView.as_view(), name="post_delete"),
]
