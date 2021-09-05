from books import models
from rest_framework import viewsets
from books.api import serializers

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()
    