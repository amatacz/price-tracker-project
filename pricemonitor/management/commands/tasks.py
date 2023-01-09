from django.core.management.base import BaseCommand, CommandError
from pricemonitor.models.serviceproduct import ServiceProductDataRequest
from pricemonitor.tasks import handle_task

class Command(BaseCommand):

    def handle(self, *args, **options):
        pendings = ServiceProductDataRequest.objects.filter(status='p')
        print(pendings)
        for task in pendings:
            handle_task.delay(task.id)

            