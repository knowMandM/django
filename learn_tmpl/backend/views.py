from django.shortcuts import render

# Create your views here.
def home(request):
    str = "hello boy!"
    return render(request, 'home.html', {"content" : str, "list" : ["1"], "show" : True})
