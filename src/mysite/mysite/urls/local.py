from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
# project.urls.baseからurlpatternsをimportする必要があります
from mysite.urls.base import urlpatterns

urlpatterns += [
    # ymlを作る
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # apiの内容を見れる
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
