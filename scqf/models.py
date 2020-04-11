from django.conf import settings
from django.db import models

class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desctiption = models.TextField()
    image_url = models.CharField(max_length=500, default='https://i.imgur.com/FChk3bD.jpg')
    grade = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def publish(self):
        self.save()


class Feedback(models.Model):
    club_id = models.IntegerField()
    author = models.CharField(max_length=50)
    text = models.TextField()
    GRADE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    grade = models.IntegerField(
        choices=GRADE_CHOICES,
        default=1,
    )

    def publish(self):
        self.save()
