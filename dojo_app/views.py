from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def results(request):
    return render(request,"results.html")

def results(request):
    context = {
        "name": request.POST['name'],
        "location": request.POST['location'],
        "language": request.POST['language'],
        "comment": request.POST['comment']
    }
    return render(request, "results.html", context) 