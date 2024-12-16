import pytest
import json
from appxxx.models import Post


@pytest.mark.django_db
class TestPostViews:
  # 一覧取得のテスト
  def test_post_view(self, client):
    response = client.get("/app/post/")
    assert response.status_code == 200
    
  # 投稿処理のテスト
  def test_post_create_view(self, client):
    response = client.post("/app/post/create/", {"description": "test"})
    assert response.status_code == 201
    
  # 一部取得のテスト
  def test_post_get_one(self, client):
    post = Post.objects.create(description="test")
    response = client.get(f"/app/post/get/{post.pk}/")
    assert response.status_code == 200
    
  # アップデートできてるかテスト putの時はjsonじゃないと上手くできないみたい
  def test_post_update(self, client):
    post = Post.objects.create(description="test")
    response = client.put(
        f"/app/post/update/{post.pk}/",
        # json.dumpsでデータをJSON文字列に変換
        data=json.dumps({"description": "updated"}),  
        content_type="application/json" 
    )
    assert response.status_code == 200
    
  # 削除できてるかテスト
  def test_post_delete(self, client):
    post = Post.objects.create(description="test")
    response = client.delete(f"/app/post/delete/{post.pk}/")
    assert response.status_code == 204
    