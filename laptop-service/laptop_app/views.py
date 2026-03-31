from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Laptop
from .serializers import LaptopSerializer


class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            laptops = Laptop.objects.filter(
                Q(name__icontains=query) |
                Q(brand__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            laptops = Laptop.objects.all()
        serializer = self.get_serializer(laptops, many=True)
        return Response(serializer.data)
