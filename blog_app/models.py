from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_by=models.DateField(auto_now=True)

