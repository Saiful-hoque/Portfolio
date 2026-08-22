from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    technology = models.CharField(max_length=150)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title