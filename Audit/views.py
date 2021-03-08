import subprocess
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from wsgiref.util import FileWrapper


class Split(APIView):
    parser_classes = (MultiPartParser,)

    @csrf_exempt
    def post(self, request):
        with open("Audit/original_track.mp3", "wb") as new_file:
            new_file.write(request.FILES['file'].read())
        subprocess.run(["spleeter", "separate", "-p", "spleeter:5stems", "-o", "output", "Audit/original_track.mp3"])
        os.remove("Audit/original_track.mp3")
        return Response(status=status.HTTP_201_CREATED)


class VocalsAudio(APIView):
    def get(self, request):
        drums = open("output/original_track/vocals.wav", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="vocals.MP3"'
        return drums_response


class DrumsAudio(APIView):
    def get(self, request):
        drums = open("output/original_track/drums.wav", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="drums.MP3"'
        return drums_response


class PianoAudio(APIView):
    def get(self, request):
        drums = open("output/original_track/piano.wav", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="piano.MP3"'
        return drums_response


class BassAudio(APIView):
    def get(self, request):
        drums = open("output/original_track/bass.wav", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="piano.MP3"'
        return drums_response


class OtherAudio(APIView):
    def get(self, request):
        drums = open("output/original_track/other.wav", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="others.MP3"'
        subprocess.run(["rm", "-r", "output"])
        return drums_response
