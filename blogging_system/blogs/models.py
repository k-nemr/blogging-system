from django.db import models


# Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length=32, help_text="Enter author name")
    subject = models.CharField(max_length=256, help_text="Enter blog subject")
    body = models.TextField(help_text="Enter blog body")

    def __str__(self):
        return self.subject
