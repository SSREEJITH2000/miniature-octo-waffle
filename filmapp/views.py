from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movie_form
from .models import movie
# Create your views here.
def movies(request):
    moviess=movie.objects.all()
    context={
        'movie_list':moviess
    }
    return render(request,'sample.html',context)

def detail(request,movie_id):
    cinema=movie.objects.get(id=movie_id)
    return render(request,'index.html',{'hey':cinema})
    # return HttpResponse('This is movie no.' % movie_id)

def add_movie(request):
    if request.method=='POST':
        names=request.POST.get('name')
        description = request.POST.get('desc')
        years = request.POST.get('year')
        images = request.FILES['image']
        movie_business=movie(name=names,desc=description,year=years,image=images)
        movie_business.save()
    return render(request,'add.html')

def updation(request,id):
    moov=movie.objects.get(id=id)
    forms=Movie_form(request.POST or None,request.FILES,instance=moov)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':moov,'form':forms})

def deletion(request,id):
    if request.method=='POST':
        out=movie.objects.get(id=id)
        out.delete()
        return redirect('/')
    return render(request,'delete.html')