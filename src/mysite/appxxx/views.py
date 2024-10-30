from django_filters import rest_framework as filters
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


# 投稿処理
class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer


# 検索機能
class PostFilter(filters.FilterSet):
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = Post
        fields = ["description"]


# 一覧取得
class PostListAPIView(generics.ListAPIView):
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


# 更新/一部更新
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 削除
class PostDeliteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
