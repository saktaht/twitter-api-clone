import pytest
import pytz
from django.utils import timezone
from appxxx.models import Post


@pytest.mark.django_db
class TestPostModel:
    #pkがあるか確認
    def test_post_create(self):
        post = Post.objects.create(description="test")
        assert post.description == "test"
        assert post.pk is not None
        assert post.created_at
        assert post.updated_at

    # created_atとupdated_atフィールドが自動的に設定されていることをテスト
    def test_auto_timestamps(self):
        post = Post.objects.create(description="test")
        post = Post.objects.create(description="test")
        now = timezone.now()

        assert (now - post.created_at).total_seconds() < 0.1
        assert (now - post.updated_at).total_seconds() < 0.1
        
    # updateがしっかりできているかテスト
    def test_update_post(self):
        post = Post.objects.create(description="Original description")
        original_created_at = post.created_at
        original_updated_at = post.updated_at

        # 更新前の時間を記録
        before_update = timezone.now()

        # 時間差を設けて、データが変更されたことを検出するために待つ
        import time
        time.sleep(0.1)

        post.description = "Updated description"
        post.save()

        # 更新後の時間を記録
        after_update = timezone.now()

        assert post.description == "Updated description"
        assert post.created_at == original_created_at
        assert original_updated_at < post.updated_at # post.updated_atはsaveされた時の時間だから長くなる
        assert before_update < post.updated_at <= after_update

    # 複数のPostオブジェクトを作れることをテスト
    def test_multiple_posts(self):
        Post.objects.create(description="Post 1")
        Post.objects.create(description="Post 2")
        assert Post.objects.count() == 2

    @pytest.mark.parametrize("description", [
        "Short post",
        "A" * 1000,  
        "",  # からのポスト
        "Post with\nnewlines",
    ])
    
    # さまざまな長さや内容の説明文をテスト
    def test_post_descriptions(self, description):
        post = Post.objects.create(description=description)
        assert post.description == description