from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.title