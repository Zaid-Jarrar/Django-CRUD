from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):

    title = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default=None,null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snack_detail', kwargs={'pk': self.pk})
