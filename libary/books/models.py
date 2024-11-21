from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    price=models.IntegerField()
    pages=models.IntegerField()
    cover=models.ImageField(upload_to="images")
    pdf=models.FileField(upload_to="pdf")