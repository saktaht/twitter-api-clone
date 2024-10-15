from django_filters import rest_framework as filter
from rest_framework import views
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


# 投稿処理
class PostCreateAPIView(generics.CreateAPIView):
  serializer_class = PostSerializer

# 一覧取得
class PostListAPIView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = [filter.DjangoFilterBackend]
  filterset_fields = '__all__'
  # もっと詳しい検索機能は本の11.3章に書いてあるらしい

#一部取得
class PostRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
#更新/一部更新
class PostUpdateAPIView(generics.UpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
#削除
class PostDeliteAPIView(generics.DestroyAPIView):
  queryset = Post.objects.all()