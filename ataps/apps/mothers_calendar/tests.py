from django_webtest import WebTest


class SMSSyncBackendView(WebTest):
    def test_sms_sync__view_responds_with_false_if_form_is_not_valid(self):
        index = self.app.get('/', user='kmike')
