from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')
def flavours(request):
    return render(request,'flavours.html')
def cake(request):
    return render(request,'cake.html')
def family(request):
    return render(request,'family.html')
