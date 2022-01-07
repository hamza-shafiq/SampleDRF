from django.db import models


class Questions(models.Model):
    QUESTION_CHOICES = (
        ('Py', 'Python'),
        ('Dj', 'Django'),
    )
    question_code = models.CharField(max_length=2, choices=QUESTION_CHOICES)
    statement = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)

    def __str__(self):
        return self.question_code
