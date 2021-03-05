from django.urls import path

from Audit.views import Split

urlpatterns = [
    path('split/', Split.as_view()),
]
