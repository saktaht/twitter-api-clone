from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

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
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
class PostUpdateAPIView(RetrieveModelMixin, UpdateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# 削除 + GET
# class PostDeliteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
class PostDeleteAPIView(RetrieveModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
