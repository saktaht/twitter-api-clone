from django_filters import rest_framework as filters
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


# 検索機能
class PostFilter(filters.FilterSet):
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = Post
        fields = ["description"]
        
# 投稿処理
class PostCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        filters.DjangoFilterBackend,
    ]
    filterset_class = PostFilter


# 一部取得
class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 更新/一部更新 + GET
class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ["get", "put", "patch"]


# 削除 + GET
class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ["get", "delete"]