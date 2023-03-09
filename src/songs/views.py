from typing import Type, Union

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from songs.models import Song


class FullSongSerializer(serializers.HyperlinkedModelSerializer):
    """A song serializer that returns any relevant fields."""

    class Meta:
        model = Song
        exclude = []  # Include all fields


class SimpleSongSerializer(serializers.HyperlinkedModelSerializer):
    """A song serializer that only returns specific fields."""

    class Meta:
        model = Song
        fields = ["url", "name", "rank", "album", "writers"]


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(
        self,
    ) -> Union[Type[FullSongSerializer], Type[SimpleSongSerializer]]:
        """Returns a different serializer dependent on authentication."""
        if self.request.user.is_authenticated:
            return FullSongSerializer
        return SimpleSongSerializer

    @action(detail=True, methods=["get"])
    def lyrics(self, _, **__) -> Response:
        song = self.get_object()
        return Response({"lyrics": song.lyrics})
