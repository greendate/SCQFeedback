from django.test import TestCase
from .models import Club, Feedback

# Create your tests here.

class GradeTestCase1(TestCase):
    def setUp(self):
        Club.objects.create(club_id = 1, grade=4.5)
        Feedback.objects.create(club_id = 1, grade = 4)
        Feedback.objects.create(club_id = 1, grade = 5)

    def test_correct_grade(self):
        clubs = Club.objects.all()
        for club in clubs:
            feedbacks = Feedback.objects.filter(club_id=club.club_id)
            sum = 0
            for feedback in feedbacks:
                sum += feedback.grade
            count = Feedback.objects.filter(club_id=club.club_id).count()
            self.assertEqual(float(club.grade), round(sum / count, 1))


class GradeTestCase2(TestCase):
    def setUp(self):
        Club.objects.create(club_id = 1, grade=2.8)
        Club.objects.create(club_id = 2, grade=2.5)
        Feedback.objects.create(club_id = 1, grade = 4)
        Feedback.objects.create(club_id = 2, grade = 3)
        Feedback.objects.create(club_id = 1, grade = 1)
        Feedback.objects.create(club_id = 2, grade = 2)
        Feedback.objects.create(club_id = 1, grade = 2)
        Feedback.objects.create(club_id = 1, grade = 4)

    def test_correct_grade(self):
        clubs = Club.objects.all()
        for club in clubs:
            feedbacks = Feedback.objects.filter(club_id=club.club_id)
            sum = 0
            for feedback in feedbacks:
                sum += feedback.grade
            count = Feedback.objects.filter(club_id=club.club_id).count()
            self.assertEqual(float(club.grade), round(sum / count, 1))
