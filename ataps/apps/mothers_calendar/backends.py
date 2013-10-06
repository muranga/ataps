from urllib import quote_plus
from django.http import HttpResponse
from django.utils import simplejson
from rapidsms.backends.base import BackendBase
from rapidsms.backends.http.views import GenericHttpBackendView

import logging
import requests
from django.conf import settings

log = logging.getLogger(__name__)


def clean_number(param):
    cleaned_num = str(param).replace("+", "")
    if cleaned_num.startswith("0"):
        cleaned_num = "256%s" % cleaned_num[1:]
    return cleaned_num


class OutGoingSmsBackend(BackendBase):
    def send(self, id_, text, identities, context={}):
        username = getattr(settings, 'SMS_USER', '')
        password = getattr(settings, 'SMS_PASSWORD', '')
        number = clean_number(identities[0])
        message = text
        code = getattr(settings, 'sms_code', "ATAPS")
        url = "https://secure.jolis.net/jc/sms/interface.php?username=%s&password=%s&command=sendsinglesms&destination=%s&message=%s&source=%s" % (
            username, password, number, quote_plus(message), code)
        print url
        r = requests.post(url, verify=False)
        print r.text


class SMSSyncBackendView(GenericHttpBackendView):
    backend_name = 'smssync'
    params = {
        'identity_name': 'from',
        'text_name': 'message',
    }

    def form_invalid(self, form):
        super(SMSSyncBackendView, self).form_invalid(form)
        response = {
            "payload": {
                "success": "false"
            }
        }
        return HttpResponse(simplejson.dumps(response), mimetype="application/json")

    def form_valid(self, form):
        super(SMSSyncBackendView, self).form_valid(form)
        response = {
            "payload": {
                "success": "true"
            }
        }
        return HttpResponse(simplejson.dumps(response), mimetype="application/json")

