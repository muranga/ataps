from rapidsms.contrib.handlers import KeywordHandler
from rapidsms.models import Contact
from ataps.apps.mothers_calendar.models import Mother
from ataps.apps.mothers_calendar.tasks import query_number_of_weeks


class MotherRegistrationHandler(KeywordHandler):
    keyword = "register|reg|join"

    def help(self):
        self.respond("To register, send JOIN ataps")

    def handle(self, text):
        contact, contact_created = Contact.objects.get_or_create(name=self.msg.connection.identity)
        try:
            mother = Mother.objects.get(contact_number=self.msg.connection.identity)
            mother.contact = contact
            mother.save()
        except Mother.DoesNotExist:
            mother = Mother.objects.create(contact_number=self.msg.connection.identity, contact=contact)
        mother, mother_created = Mother.objects.get_or_create(contact_number=self.msg.connection.identity)

        self.msg.connection.contact = contact
        self.msg.connection.save()
        if mother_created:
            self.respond("Thank you for registering with ATAPS !")
            query_number_of_weeks.delay(mother)
        else:
            self.respond("Thank you. You are already registered with ATAPS !")