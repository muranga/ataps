from rapidsms.apps.base import AppBase
from ataps.apps.mothers_calendar.models import QuestionResponse


class ATAPS(AppBase):
    def handle(self, msg):
        try:
            responses = msg.connections[0].contact.responses.filter(sent=True, responded=False)
            question_response = responses[0]
            question_response.response = msg.text
            question_response.responded = True
            question_response.save()
            return True
        except(QuestionResponse.DoesNotExist, AttributeError):
            return False
