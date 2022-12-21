from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250, blank=True)
    content = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    method = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',
                              default='../default_post_wmlygq', blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
