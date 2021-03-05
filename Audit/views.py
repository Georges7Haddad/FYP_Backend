from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from wsgiref.util import FileWrapper


class Split(APIView):
    parser_classes = (MultiPartParser, )

    @csrf_exempt
    def post(self, request):
        # with open("Audit/new.mp3", "wb") as new_file:
        #     new_file.write(request.FILES['file'].read())
        vocals = open("Audit/rap.MP3", "rb")
        vocals_response = HttpResponse(FileWrapper(vocals), content_type="audio/mpeg", status=status.HTTP_201_CREATED)
        vocals_response['Content-Disposition'] = 'attachment; filename="rap.MP3"'
        return vocals_response

    def get(self, request):
        drums = open("Audit/Kzood.MP3", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="rap.MP3"'
        return drums_response
