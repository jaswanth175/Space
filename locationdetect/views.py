from .models import MapsDB
from .serializer import MapsDBSerializer,UserDBSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
def location(request):
    if request.method == "GET":
        dataDB = MapsDB.objects.all()
        ser = MapsDBSerializer(dataDB,many=True)
        print(ser.data)
        return JsonResponse({"data":ser.data},status=200)


class HelloView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        content = {'message': 'Hello, World!'}
        return Response(content)