from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
class leave_request(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    course_choices = (
        ('','select your course'),
        ('AI', 'Artificial Intelligence and Machine Learning'),
        ('IOT', 'Cybersecurity and Internet of Things'),
    )
    course = models.CharField(max_length=30,choices=course_choices)
    mentor_choices=(
        ('','select your mentor'),
        ('mentor1', 'mentor1'),
        ('mentor2', 'mentor2'),
    )
    mentor=models.CharField(max_length=100, choices=mentor_choices)
    leaves=models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    start_date=models.CharField(max_length=30)
    end_date=models.CharField(max_length=30)
    reason=models.TextField()



