from django.urls import path

from .views import (
    PostCreateAndListAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
)


urlpatterns = [
    path("", PostCreateAndListAPIView.as_view(), name="post_list"),
    path("get/<int:pk>/", PostRetrieveAPIView.as_view(), name="post_get"),
    path("update/<int:pk>/", PostUpdateAPIView.as_view(), name="post_update"),
    path("delete/<int:pk>/", PostDeleteAPIView.as_view(), name="post_delete"),
]
