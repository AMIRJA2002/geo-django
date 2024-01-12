from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Public
from django.contrib.gis.geos import Point
from pyproj import Transformer


class SearchForZoneInformation(APIView):
    class InputSerializer(serializers.Serializer):
        lat = serializers.FloatField()
        long = serializers.FloatField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Public
            exclude = ('wkb_geometry',)

    def get(self, request):
        data = self.InputSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        # Transformer point from 4326 to 32639
        proj = Transformer.from_crs(4326, 32639)
        x1, y1 = (data.validated_data.get('lat'), data.validated_data.get('long'))
        x2, y2 = proj.transform(x1, y1)

        point = Point(x=x2, y=y2, srid=32639)
        poly = Public.objects.filter(wkb_geometry__contains=point)

        ser_data = self.OutputSerializer(poly, many=True)
        return Response(ser_data.data)
