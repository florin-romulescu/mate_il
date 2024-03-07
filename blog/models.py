import datetime
from django.db import models

# This file is used for defining the models of our application.

class Post(models.Model):
    """
    The model class for the posts table.
    """

    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField("date published", null=False)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    attachments = models.ManyToManyField("Attachment", related_name="posts", blank=True)

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author}"


class Tag(models.Model):
    """
    The model class for the tags table.
    """

    name = models.CharField(max_length=31, primary_key=True)
    color = models.CharField(max_length=6, null=False)

    def __str__(self) -> str:
        return "{%s}" % self.name
    

class Attachment(models.Model):
    
    file = models.FileField(upload_to="attachments/")
    description = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.description
