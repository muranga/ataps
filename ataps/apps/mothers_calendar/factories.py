import factory
from rapidsms.models import Contact
from ataps.apps.mothers_calendar.models import Mother, WeekNumber, QuestionType, Question


class WeekFactory(factory.Factory):
    FACTORY_FOR = WeekNumber
    week_number = "1"


class ContactFactory(factory.Factory):
    FACTORY_FOR = Contact
    name = "0783010831"


class MotherFactory(factory.Factory):
    FACTORY_FOR = Mother
    contact_number = '0783010831'
    contact = factory.SubFactory(ContactFactory)
    week = factory.SubFactory(WeekFactory)


class QuestionTypeFactory(factory.Factory):
    FACTORY_FOR = QuestionType
    q_type = "week"


class QuestionFactory(factory.Factory):
    FACTORY_FOR = Question
    question_text = "week"
    question_type = factory.SubFactory(QuestionTypeFactory)