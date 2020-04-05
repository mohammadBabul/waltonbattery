from rest_framework import serializers
from battery.models import BatteryDataSet
from battery.models import Category
from battery.models import Result



class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryDataSet
        fields =('__all__')        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('__all__')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =('__all__')   