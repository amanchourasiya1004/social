from django.shortcuts import render, redirect
from .models import Track
import datetime
# Create your views here.

def index(request):
    track = Track.objects.all()
    if(request.method == 'POST'):
        user = request.POST.get('name')
        tr = Track(username = user)
        tr.save()
        return redirect('index')
    return render(request, 'index.html', {'track' : track})