from django.urls import path
from .views import letterList, oneLetter

urlpatterns = [
    path('words/', letterList.as_view(), name="words"),
    path('words/<name>/', oneLetter.as_view(), name="name"),
]