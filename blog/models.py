from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):

    # properties of the blog post:
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    # methods of the blog post:

    # the publish() method records the current time when the post was published
    # also calls save() function to save the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # printing the Post object will return a string with the title of the Post
    def __str__(self):
        return self.title
