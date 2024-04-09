from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
