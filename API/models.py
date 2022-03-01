from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.



class unique_id(models.Model):
    user_id = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user_id)


class video_data(models.Model):
    user_id = models.ForeignKey(unique_id, default=None, on_delete=models.CASCADE)
    video_url = models.URLField(max_length=5000)
    date_created = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return str(self.user_id)