from django.db import models

# Create your models here.
class Track(models.Model):
    username = models.CharField(max_length = 16)

    def __str__(self):
        return self.username + ' | ' + str(self.pk)