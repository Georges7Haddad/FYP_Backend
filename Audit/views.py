import subprocess
import os
from random import randrange
from threading import Timer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from wsgiref.util import FileWrapper


def delete_output(rand):
    subprocess.run(["rm", "-r", f"output{rand}"])


class Split(APIView):
    parser_classes = (MultiPartParser,)

    @csrf_exempt
    def post(self, request):
        rand = randrange(1000)
        with open(f"Audit/original_track{rand}.mp3", "wb") as new_file:
            new_file.write(request.FILES['file'].read())
        subprocess.run(
            ["spleeter", "separate", "-p", "spleeter:5stems", "-o", f"output{rand}", f"Audit/original_track{rand}.mp3"])
        os.remove(f"Audit/original_track{rand}.mp3")
        t = Timer(900.0, delete_output, args=[rand])
        t.start()
        return Response({"rand": rand}, status=status.HTTP_201_CREATED)


class VocalsAudio(APIView):
    def get(self, request, rand):
        vocals = open(f"output{rand}/original_track{rand}/vocals.wav", "rb")
        vocals_response = HttpResponse(FileWrapper(vocals), content_type="audio/mpeg", status=status.HTTP_200_OK)
        vocals_response['Content-Disposition'] = 'attachment; filename="vocals.MP3"'
        return vocals_response


class DrumsAudio(APIView):
    def get(self, request, rand):
        drums = open(f"output{rand}/original_track{rand}/drums.wav", "rb")
        drums_response = HttpResponse(FileWrapper(drums), content_type="audio/mpeg", status=status.HTTP_200_OK)
        drums_response['Content-Disposition'] = 'attachment; filename="drums.MP3"'
        return drums_response


class PianoAudio(APIView):
    def get(self, request, rand):
        piano = open(f"output{rand}/original_track{rand}/piano.wav", "rb")
        piano_response = HttpResponse(FileWrapper(piano), content_type="audio/mpeg", status=status.HTTP_200_OK)
        piano_response['Content-Disposition'] = 'attachment; filename="piano.MP3"'
        return piano_response


class BassAudio(APIView):
    def get(self, request, rand):
        bass = open(f"output{rand}/original_track{rand}/bass.wav", "rb")
        bass_response = HttpResponse(FileWrapper(bass), content_type="audio/mpeg", status=status.HTTP_200_OK)
        bass_response['Content-Disposition'] = 'attachment; filename="piano.MP3"'
        return bass_response


class OtherAudio(APIView):
    def get(self, request, rand):
        other = open(f"output{rand}/original_track{rand}/other.wav", "rb")
        other_response = HttpResponse(FileWrapper(other), content_type="audio/mpeg", status=status.HTTP_200_OK)
        other_response['Content-Disposition'] = 'attachment; filename="others.MP3"'
        return other_response
