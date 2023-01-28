from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    original_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment_image = models.ImageField(upload_to='images/',
                                      default='../default_post_wmlygq',
                                      blank=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
