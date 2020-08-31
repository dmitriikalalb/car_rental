from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Auto
from .serializers import CarSerializer


# Create your views here.
def index(request):
    return render(request, 'cars/index.html')


class CarView(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = CarSerializer


def car(request):
    return render(request, 'cars/cars.html')
