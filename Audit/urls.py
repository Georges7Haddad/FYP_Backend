from django.urls import path

from Audit.views import *

urlpatterns = [
    path('split/', Split.as_view()),
    path('vocals/<int:rand>/', VocalsAudio.as_view()),
    path('drums/<int:rand>/', DrumsAudio.as_view()),
    path('piano/<int:rand>/', PianoAudio.as_view()),
    path('bass/<int:rand>/', BassAudio.as_view()),
    path('other/<int:rand>/', OtherAudio.as_view()),
]
