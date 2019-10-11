from django.db import models
# Create your models here.

class Letter(models.Model):
    name = models.CharField(null=False, max_length=1)

    def __str__(self):
        return self.name

class Word(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField()
    sources = models.CharField(max_length=300, blank=True, null=True)
    letter = models.ForeignKey(Letter, related_name='words', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name