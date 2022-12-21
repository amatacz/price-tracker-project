from django.core.management.base import BaseCommand, CommandError
from pricemonitor.models.serviceproduct import ServiceProductDataRequest

class Command(BaseCommand):

    def handle(self, *args, **options):
        pendings = ServiceProductDataRequest.objects.filter(status='p')

        for task in pendings:
            task.get_data()