from django.core.management import BaseCommand
from ataps.apps.mothers_calendar.models import QuestionResponse


class Command(BaseCommand):
    def handle(self, *args, **options):
        un_started = QuestionResponse.objects.filter(sent=False)
        for resp in un_started:
            resp.send()
