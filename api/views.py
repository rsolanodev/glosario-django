from .models import Letter
from .serializers import LetterSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

class letterList(generics.ListAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class oneLetter(generics.ListAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

    def get(self, request, *args, **kwargs):
        try:
            letter = self.queryset.get(name=kwargs["name"])
            return Response(LetterSerializer(letter).data)
        except Letter.DoesNotExist:
            return Response(
                data={
                    "message": "Letter with name: {} does not exist".format(kwargs["name"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
