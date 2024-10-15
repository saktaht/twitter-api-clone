from django.contrib import admin
from django.urls import path, include
# https://github.com/jazzband/djangorestframework-simplejwt ソースコード
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # トークンの取得
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # トークンの再取得
    path("app/", include("app.urls")),
]