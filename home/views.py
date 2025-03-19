from django.shortcuts import render

# Create your views here.
def baseview(request):
    return render(request, 'base.html')

def homeview(request):
    return render(request, 'components/home.html')

def workview(request):
    return render(request, 'components/work.html')

def aboutview(request):
    return render(request, 'components/about.html')

def contactview(request):
    return render(request, 'footer.html')

