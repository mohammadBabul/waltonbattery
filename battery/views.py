import csv
import io
from django.shortcuts import render
from django.contrib import messages
from battery.models import BatteryDataSet
from battery.models import Category
# Create your views here.
# one parameter named request


def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = BatteryDataSet.objects.all()
    

# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be serian_no, time,charging_level,temperature,battery_voltage,decreased_voltage,charging_status',
        'profiles': data
      
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = BatteryDataSet.objects.update_or_create(
            serial_no=column[0],
            time=column[1],
            charging_level=column[2],
            temperature=column[3],
            battery_voltage=column[4],
            decreased_voltage=column[5],
            charging_status=column[6],
            
        )
    context = {}
    return render(request, 'home.html', context)


def home_page(request):
    # declaring template
    context = {}

    return render(request, 'home.html', context)