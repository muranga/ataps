from django.db import models
import rapidsms
from rapidsms.models import Contact, Connection

WEEK = "WEEK"

GENERAL = "general"

NUMERICAL = "numerical"

YES_NO = "yes_no"


class WeekNumber(models.Model):
    week_number = models.IntegerField()

    def __str__(self):
        return str(self.week_number)


class Message(models.Model):
    message_text = models.CharField(max_length=120)
    week = models.ForeignKey(WeekNumber, related_name="week_in_cycle")

    def __str__(self):
        return self.message_text


class QuestionType(models.Model):
    QUESTIONTYPE = (
        (YES_NO, "Yes or No Response"),
        (NUMERICAL, "Numerical Response" ),
        (GENERAL, "Generic Response"),
        (WEEK, "Numerical Response"),

    )

    q_type = models.CharField(max_length=120, choices=QUESTIONTYPE, unique=True)

    def __str__(self):
        return self.q_type


class Question(models.Model):
    question_type = models.ForeignKey(QuestionType)
    week = models.ForeignKey(WeekNumber, related_name="weeks_question", default=0)
    question_text = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.question_text


class Mother(models.Model):
    contact_number = models.CharField(max_length=120, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, related_name="mothers")
    week = models.ForeignKey(WeekNumber, related_name="mothers", default=0)

    def __str__(self):
        return self.contact_number


class QuestionResponse(models.Model):
    contact = models.ForeignKey(Contact, related_name="responses")
    response = models.CharField(max_length=255, null=True, blank=True)
    responded = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name="responses")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("question", "contact"),)

    def send(self):
        try:
            connection = self.contact.connections.all()[0]
            rapidsms.router.send(self.question.question_text, connection)
            self.sent = True
            self.save()
        except Connection.DoesNotExist:
            pass
