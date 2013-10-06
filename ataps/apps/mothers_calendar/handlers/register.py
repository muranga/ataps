from rapidsms.contrib.handlers import KeywordHandler
from rapidsms.models import Contact
from ataps.apps.mothers_calendar.models import Mother, WeekNumber
from ataps.apps.mothers_calendar.tasks import query_number_of_weeks


class MotherRegistrationHandler(KeywordHandler):
    keyword = "register|reg|join"

    def help(self):
        self.respond("To register, send JOIN ataps")

    def handle(self, text):
        contact, contact_created = Contact.objects.get_or_create(name=self.msg.connection.identity)
        week, created = WeekNumber.objects.get_or_create(week_number=0)
        try:
            mother = Mother.objects.get(contact_number=self.msg.connection.identity)
            mother.contact = contact
            mother.save()
            mother_created = False
        except Mother.DoesNotExist:
            mother = Mother.objects.create(contact_number=self.msg.connection.identity, contact=contact, week=week)
            mother_created = True

        self.msg.connection.contact = contact
        self.msg.connection.save()
        if mother_created:
            self.respond("Thank you for registering with ATAPS !")
	    query_number_of_weeks(mother)
        else:
            self.respond("Thank you. You are already registered with ATAPS !")