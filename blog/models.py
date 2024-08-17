import datetime
from django.db import models

# This file is used for defining the models of our application.

class Post(models.Model):
    """
    The model class for the posts table.
    
    Attributes:
        - title: An unique name for the post
        - author: The name of the person who uploaded the file
        - pub_date: When the file was uploaded
        - tags: All the tags related to this post
        - attachments: Al the attachments related to this post
    """

    title = models.TextField(default="", null=False)
    author = models.CharField(max_length=255, null=True)
    description = models.TextField(default="", null=False)
    pub_date = models.DateTimeField("date published", null=False)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    attachments = models.ManyToManyField("Attachment", related_name="posts", blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    
    @property
    def short_description(self) -> str:
        MAX_LENTH:int = 400
        return (
                self.description[:MAX_LENTH] + "..." if len(self.description) > MAX_LENTH
                else self.description
                )
        
    @classmethod
    def get_posts_by_tag(cls, tag_name:str):
        return cls.objects.filter(tags__name = tag_name)

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author}"


class Tag(models.Model):
    """
    The model class for the tags table.
    
    Attributes:
        - name: The name assigned to the color
        - color: a hex string to represent a color (example ffe1a7)
        - posts: all the posts that uses this tag (from many to many relationship)
    """

    name = models.CharField(max_length=31, primary_key=True)
    
    @property
    def short_name(self) -> str:
        MAX_LENGTH: int = 6
        return (
            self.name[:MAX_LENGTH] + '...' if len(self.name) > MAX_LENGTH
            else self.name
        )

    def __str__(self) -> str:
        return "{%s}" % self.name
    

class Attachment(models.Model):
    """
    The model class for the attachments table.
    
    Attributes:
        - file: The representation of the file in the os
        - description: A representative description of this file
        - posts: all the posts that uses this attachment (from many to many relationship)
    """
    
    file = models.FileField(upload_to="attachments/")
    description = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.description
