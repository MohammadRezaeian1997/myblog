from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.article.title}"
