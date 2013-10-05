from django.http import HttpResponse
from django.utils import simplejson
from rapidsms.backends.base import BackendBase
from rapidsms.backends.http.views import GenericHttpBackendView

import logging

log = logging.getLogger(__name__)


class OutGoingSmsBackend(BackendBase):
    def send(self, id_, text, identities, context={}):
        return super(OutGoingSmsBackend, self).send(id_, text, identities, context)


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

