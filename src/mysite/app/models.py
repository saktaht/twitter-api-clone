from django.db import models


class Post(models.Model):
    class Meta:
        app_label = "app"  # これを書かないとmigrateできなくなる
        db_table = "post"

    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
