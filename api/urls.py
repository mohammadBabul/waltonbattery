from django.urls import path
from .views import BatteryAPIView
from .views import CategoryAPIView
from .views import ResultAPINewView



urlpatterns = [
    path('model/', CategoryAPIView.as_view()),
    #path('quotes/<int:pk>/', QuoteAPIDetailView.as_view()),
    path('new/', ResultAPINewView.as_view()),
    path('batterydata/', BatteryAPIView.as_view()),
] 