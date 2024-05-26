from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    price = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
