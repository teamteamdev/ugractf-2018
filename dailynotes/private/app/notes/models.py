from django.db import models


class Note(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
