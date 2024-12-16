import pytest
from appxxx.models import Post
from appxxx.serializers import PostSerializer


@pytest.mark.django_db
class TestPostSerializers:
  # シリアライズできているかテスト
  def test_post_valid(self):
    post = Post.objects.create(description="test")
    serializer = PostSerializer(instance=post)
    data = serializer.data
    
    assert data["description"] == "test"
    assert "id" in data
    
  # タイトルがからの場合のテスト
  def test_post_invalid(self):
    invalid_data = {"description": ""}
    serializer = PostSerializer(data=invalid_data)
    
    assert not serializer.is_valid() 
    assert "description" in serializer.errors
    
  # オブジェクトがデータベースに正しく保存され、タイトルが期待通りであることを確認
  def test_post_create(self):
    post = {"description": "test"}
    serializer = PostSerializer(data=post)
    
    assert serializer.is_valid()
    task = serializer.save()
    assert task.description == "test"
    assert Post.objects.count() == 1