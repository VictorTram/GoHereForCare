from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.

class Section(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_Num = models.IntegerField();
    title = models.CharField(max_length=200)
    #text = models.TextField()
    publish = models.BooleanField(default=True, null=True)
    text =HTMLField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

