from django.core.management.base import BaseCommand
from pricemonitor.models.serviceproduct import ServiceProductDataRequest

class Command(BaseCommand):
    def handle(self, *args, **options):
        return ServiceProductDataRequest.objects.register_tasks()

        #przez crona