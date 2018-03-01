from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
	customers = Customer.objects.all()
	return render(request, 'index.html', {'customers' : customers})