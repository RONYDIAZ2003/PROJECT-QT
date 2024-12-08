from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skill_1 = models.CharField(max_length=100)
    skill_2 = models.CharField(max_length=100)
    skill_3 = models.CharField(max_length=100)
    skill_4 = models.CharField(max_length=100)
    skill_5 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

