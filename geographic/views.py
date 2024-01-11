from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Public
from django.contrib.gis.geos import Point


class CreateDatabaseData(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'od': 'ok'})


class SearchForZoneInformation(APIView):
    class InputSerializer(serializers.Serializer):
        lat = serializers.FloatField()
        long = serializers.FloatField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Public
            fields = '__all__'

    def get(self, request):
        data = self.InputSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        lat = data.validated_data.get('lat')
        long = data.validated_data.get('long')
        point = Point(x=lat, y=long, srid=32639)
        public = Public.objects.filter(wkb_geometry__contains=point)

        ser_data = self.OutputSerializer(public, many=True)
        return Response(ser_data.data)


