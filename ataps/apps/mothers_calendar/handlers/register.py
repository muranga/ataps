from rapidsms.contrib.handlers import KeywordHandler
from rapidsms.models import Contact
from ataps.apps.mothers_calendar.models import Mother


class MotherRegistrationHandler(KeywordHandler):
    keyword = "register|reg|join"

    def help(self):
        self.respond("To register, send JOIN ataps")

    def handle(self, text):
        contact, contact_created = Contact.objects.get_or_create(name=self.msg.connection.identity)
        mother, mother_created = Mother.objects.get_or_create(contact_number=self.msg.connection.identity, contact=contact)
        self.msg.connection.contact = contact
        self.msg.connection.save()

        self.respond(
            "Thank you for registering with ATAPS !")