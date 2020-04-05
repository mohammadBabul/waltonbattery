from rest_framework import generics
from battery.models import BatteryDataSet
from battery.models import Category
from battery.models import Result
from .selializers import BatterySerializer
from .selializers import CategorySerializer
from .selializers import ResultSerializer


class BatteryAPIView(generics.ListAPIView):
    queryset = BatteryDataSet.objects.all().order_by('id')
    serializer_class = BatterySerializer 

 


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ResultAPINewView(generics.ListCreateAPIView):
    queryset = Result.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = ResultSerializer





   