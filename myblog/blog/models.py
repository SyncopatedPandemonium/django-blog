from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.date:%B %d, %Y}'
