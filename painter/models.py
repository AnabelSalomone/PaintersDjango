from django.db import models

# Create your models here.
class Painter(models.Model):
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.firstname + " " + self.surname