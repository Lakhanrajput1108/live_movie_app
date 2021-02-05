from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .import forms
from .models import MovieInfo
# Create your views here.
def display(request):
    global form
    form=forms.MovieInfo()
    my_dict={'form':form}
    form=forms.MovieInfo(request.POST)
    return render(request,'movie_app/film.html', context=my_dict)

def display_list(request):
    Movie_Info=MovieInfo.objects.all()
    return render(request,'movie_app/Movie_list.html',{'movieinfo':Movie_Info})

def add_new_movie(request):
        #global
        form=forms.MovieResForms()
        if request.method=='POST':
            form=forms.MovieResForms(request.POST)
            if form.is_valid():
                print("\n\n**************  Okkkkk  ********************")
                form.save()
                print("Data Inserted Successfully\n")
                return redirect('http://127.0.0.1:8000/')
        return render(request,'movie_app/add_movie.html',{'form':form})


def add_review(request):
        #global
        form=forms.RatingForms()
        if request.method=='POST':
            form=forms.RatingForms(request.POST)
            if form.is_valid():
                print("\n\n**************  Okkkkk  ********************")
                form.save()
                print("REVIEW Inserted Successfully\n")
                return redirect('movie/')
        return render(request,'movie_app/review.html',{'form':form})

def about_us(request):
    return render(request,'movie_app/about.html')
