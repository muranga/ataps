from django.core.urlresolvers import reverse
from django.utils import simplejson
from django_webtest import WebTest


class SMSSyncBackendView(WebTest):
    def test_sms_sync_view_responds_with_false_if_form_is_not_valid(self):
        index = self.app.post(reverse("smssync-backend"))
        data = simplejson.loads(index.content)
        self.assertEquals("false", data['payload']['success'])

    def test_sms_sync_view_responds_with_true_if_valid_information_is_sent(self):
        index = self.app.post(reverse("smssync-backend"), {'message': "hello", 'from': '999'})
        data = simplejson.loads(index.content)
        self.assertEquals("true", data['payload']['success'])