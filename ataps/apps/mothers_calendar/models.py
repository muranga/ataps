from django.db import models
from rapidsms.models import Contact


class WeekNumber(models.Model):
    week_number = models.IntegerField()

    def __str__(self):
        return self.week_number


class Message(models.Model):
    message_text = models.CharField(max_length=120)
    week = models.ForeignKey(WeekNumber, related_name="week_in_cycle")

    def __str__(self):
        return self.message_text


class QuestionType(models.Model):
    QUESTIONTYPE = (
        ("yes_no", "Yes or No Response"),
        ("numerical", "Numerical Response" ),
        ("general", "Generic Response"),

    )

    q_type = models.CharField(max_length=120, choices=QUESTIONTYPE)

    def __str__(self):
        return self.q_type


class Question(models.Model):
    question_type = models.ForeignKey(QuestionType)
    week = models.ForeignKey(WeekNumber, related_name="weeks_question")
    question_text = models.CharField(max_length=120)

    def __str__(self):
        return self.q_type


class Mother(models.Model):
    contact_number = models.CharField(max_length=120, unique=True)
    week_number = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact)
