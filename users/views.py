from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'users/index.html')
# def about(request):
#     return HttpResponse("this is users about page")