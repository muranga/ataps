from django.core.urlresolvers import reverse
from django.utils import simplejson
from django_webtest import WebTest
from ataps.apps.mothers_calendar.factories import MotherFactory, ContactFactory
from ataps.apps.mothers_calendar.models import QuestionResponse
from ataps.apps.mothers_calendar.tasks import query_number_of_weeks, WEEKS_PREGNANT_ARE_YOU_QUESTION


class SMSSyncBackendView(WebTest):
    def test_sms_sync_view_responds_with_false_if_form_is_not_valid(self):
        index = self.app.post(reverse("smssync-backend"))
        data = simplejson.loads(index.content)
        self.assertEquals("false", data['payload']['success'])

    def test_sms_sync_view_responds_with_true_if_valid_information_is_sent(self):
        index = self.app.post(reverse("smssync-backend"), {'message': "hj", 'from': '0783010831'})
        data = simplejson.loads(index.content)
        self.assertEquals("true", data['payload']['success'])

    def test_that_when_the_query_number_of_weeks_task_is_run_a_question_response_is_created(self):
        contact = ContactFactory.build()
        contact.save()
        mother = MotherFactory.create(contact=contact)
        query_number_of_weeks(mother)
        self.assertEquals(1, QuestionResponse.objects.filter(contact=mother.contact, sent=False,
                                                             question__question_text=WEEKS_PREGNANT_ARE_YOU_QUESTION).count())