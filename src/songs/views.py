from rest_framework import serializers, viewsets

from songs.models import Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """A model serializer for beatles songs."""

    class Meta:
        model = Song
        exclude = []


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
