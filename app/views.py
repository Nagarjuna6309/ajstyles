from django.shortcuts import render

# Create your views here.
def ajstyles(request):
    d={'names':'TEJA'}
    return render(request,'ajstyles.html',d)