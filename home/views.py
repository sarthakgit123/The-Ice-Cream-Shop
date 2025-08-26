from django.shortcuts import render,HttpResponse
from home.models import Contact

def index(request):
    if request.method=="POST":
        email=request.POST.get('email')
        reviews=request.POST.get('reviews')
        contact=Contact(email=email,reviews=reviews)
        contact.save()
    return render(request,'index.html')
def flavours(request):
    return render(request,'flavours.html')
def cake(request):
    return render(request,'cake.html')
def family(request):
    return render(request,'family.html')
