from rest_framework import viewsets
# Create your views here.
from utils.defaultviewset import DefaultViewSet, get_keywords
from notes import serializers
from notes import models


class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NotesSerializer
    queryset = models.Notes.objects.all()

    def get_queryset(self):
        params = self.request.query_params
        queryset = self.queryset.filter(user=self.request.user)
        search_map = {
            'title__contains': 'title'
        }
        keywords = get_keywords(search_map, params)
        return queryset.filter(**keywords)


