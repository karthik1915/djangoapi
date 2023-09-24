from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    category = models.CharField(max_length=100)
    tags = models.JSONField(default=list)  # Use JSONField to store tags as an array

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(
        max_length=50,
        choices=[("vent", "Vent"), ("poems", "Poems"), ("convo", "Convo")],
        default="",
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    authorname = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="post")
    tags = models.JSONField(default=list)

    def __str__(self):
        return self.title
