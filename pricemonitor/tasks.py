from django.conf import settings
from pricetracker import celery_app
from pricemonitor.management.commands import serviceproductdatarequest
from pricemonitor.models.serviceproduct import ServiceProductDataRequest


@celery_app.task(serializer='json')
def handle_task(task_id):
    obj = ServiceProductDataRequest.objects.get(id=task_id)
    result = obj.get_data()
    print(result)
    #logger biblioteka do uzupełnienia
    return {"status": True}
