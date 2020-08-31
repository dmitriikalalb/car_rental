from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('api/cars', views.CarView)
app_name = 'cars'
urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.car, name='car'),
]

urlpatterns += router.urls
