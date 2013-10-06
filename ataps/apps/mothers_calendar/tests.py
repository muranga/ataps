from django.core.urlresolvers import reverse
from django.utils import simplejson
from django_webtest import WebTest
from rapidsms.models import Backend, Connection
from ataps.apps.mothers_calendar.factories import MotherFactory, ContactFactory, QuestionTypeFactory, QuestionFactory
from ataps.apps.mothers_calendar.models import QuestionResponse, Mother
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

    def test_that_when_a_question_has_been_sent_and_has_not_yet_been_responded_to_it_receives_a_message_to_the_user(
            self):
        backend, created = Backend.objects.get_or_create(name="smssync")
        contact = ContactFactory.build()
        contact.save()
        connection, created = Connection.objects.get_or_create(identity="0783010831", backend=backend)
        connection.contact = contact
        connection.save()
        q_type = QuestionTypeFactory.build()
        q_type.save()
        question = QuestionFactory.build(question_type=q_type)
        question.save()
        resp = QuestionResponse.objects.create(contact=contact, question=question, sent=True)
        message = "hj"
        index = self.app.post(reverse("smssync-backend"), {'message': message, 'from': '0783010831'})
        self.assertEquals(message, QuestionResponse.objects.get(id=resp.id).response)

    def test_that_when_you_send_join_you_get_registered_as_a_mother(self):
        number = '0783010831'
        index = self.app.post(reverse("smssync-backend"), {'message': "join ataps", 'from': number})
        self.assertEquals(1, Mother.objects.filter(contact_number=number).count())



