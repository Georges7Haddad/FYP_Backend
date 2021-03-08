from django.urls import path

from Audit.views import *

urlpatterns = [
    path('split/', Split.as_view()),
    path('vocals/', VocalsAudio.as_view()),
    path('drums/', DrumsAudio.as_view()),
    path('piano/', PianoAudio.as_view()),
    path('bass/', BassAudio.as_view()),
    path('other/', OtherAudio.as_view()),
]
