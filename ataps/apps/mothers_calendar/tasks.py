from ataps.apps.mothers_calendar.models import QuestionType, WEEK, Question, QuestionResponse

WEEKS_PREGNANT_ARE_YOU_QUESTION = "How many weeks pregnant are you ?"


def query_number_of_weeks(mother):
    question_type, created = QuestionType.objects.get_or_create(q_type=WEEK)
    question, question_created = Question.objects.get_or_create(question_text=WEEKS_PREGNANT_ARE_YOU_QUESTION,
                                                                question_type=question_type)
    print mother.contact.id
    status = QuestionResponse.objects.create(question=question, contact=mother.contact)