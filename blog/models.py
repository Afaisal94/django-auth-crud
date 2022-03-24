from django.db import models
from autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    article = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title