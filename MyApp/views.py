from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return HttpResponse("This is the place holder for blogs")

def root(request):
	return redirect("/blogs")

def new(request):
    return HttpResponse("This is a  place form for the forms of the blogs")

def create(request):
    return redirect("/") 

def show(request, number):
    return HttpResponse(f'The blog number is {number}')
    #redirect("/{number}")

def edit(request, number):
    return HttpResponse(f'This is the place hold to edit the blog number {number}')
    #redirect("/{number}")

def destroy(request, number):
    return redirect('/blogs')

def responseJson(request):
    data = [{'Date Created':'2021/07/29', 'Created by': 'Ruben Miranda'}, {'first updated': 'sooner', 'Learning purpose': 'Yes'}]
    return JsonResponse({'data':data})
        