import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Programers


@csrf_exempt
def programer_view(request):
    if request.method == "GET":
        result = {
            "programers": [
                {"id": p.id, "name": p.name, "email": p.email, "position": p.position}
                for p in Programers.objects.all()
            ]
        }
        return JsonResponse(result, status=200)
    return HttpResponse(status=405)
