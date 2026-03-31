from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Mobile
from .serializers import MobileSerializer


class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            mobiles = Mobile.objects.filter(
                Q(name__icontains=query) |
                Q(brand__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            mobiles = Mobile.objects.all()
        serializer = self.get_serializer(mobiles, many=True)
        return Response(serializer.data)
