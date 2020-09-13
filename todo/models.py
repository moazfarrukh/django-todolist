from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.


class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=125)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"Todo object {self.id}"

    def get_absolute_url(self):
        return reverse('home')
