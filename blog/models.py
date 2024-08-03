from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Article(models.Model):
    category_id = models.ForeignKey(category,on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    content = models.TextField()
    cover_image= models.FileField(upload_to='uploads/')

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    is_active= models.BooleanField(default=True)
    def __str__(self):
        return self.title
