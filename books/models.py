from django.db import models

# Create your models here.
class Book(models.Model) :
    title = models.CharField(max_length=255)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=255, null=True)
    shortDescription = models.CharField(max_length=255, null=True)
    longDescription = models.TextField(null=True)

    def __str__(self):
        return self.title


class Review(models.Model) :
    bookId = models.BigIntegerField(default=0)
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now=True, null=True)
