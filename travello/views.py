from django.shortcuts import render
from . models import Destination
# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = "Mumbai"
    # dest1.img = "destination_1.jpg"
    # dest1.desc = "The city that never sleeps"
    # dest1.price = 1000
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "Delhi"
    # dest2.img = "destination_4.jpg"
    # dest2.desc = "Full of romance and adventure"
    # dest2.price = "500"
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Lucknow"
    # dest3.img = "destination_2.jpg"
    # dest3.desc = "Full of romance"
    # dest3.price = "400"
    # dest3.offer = True
    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests' : dests})

