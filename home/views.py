from django.shortcuts import render , redirect
from .models import *
from .form import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def login(request):
    return render(request , 'login.html')

def blog(request):
    data = BlogModel.objects.all()
    return render(request,'index.html',context={'data':data})

def view(request,slug):
    data = BlogModel.objects.filter(slug = slug)
    return render(request,'view_blog.html',context = {'data':data})


def admin(request):
    try:
        if request.method=='POST':
            print(request.user)
            form = Blog_form(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            if form.is_valid():
                content = form.cleaned_data['content']
            blog_obj = BlogModel.objects.create(
                content = content , image=image , title = title ,created_by = request.user
            )
            return redirect('/add_blog/')

    except Exception as e:
        print(e)
    data = BlogModel.objects.all()
    return render(request,'add_blog.html',context = {'form':Blog_form,'data':data})


def delete(request,slug):
    try:
        data = BlogModel.objects.filter(slug = slug).delete()
        return redirect('/add_blog/')
    except Exception as e:
        print(e)
    return redirect('/add_blog/')

def edit(request,slug):
    try:
        if request.method=='POST':
            form = Blog_form(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            if form.is_valid():
                content = form.cleaned_data['content']
                object = BlogModel.objects.get(slug = slug)
                object.content = content
                object.image = image
                object.title = title
                object.save()
            return redirect('/add_blog/')
        else:
            blog_obj = BlogModel.objects.get(slug = slug)
            initial = {'content':blog_obj.content}
            form = Blog_form(initial=initial)
            return render(request,'edit.html',context = {'form':form,'title':blog_obj.title,'image':blog_obj.image})
    except Exception as e:
        print(e)
        return redirect('/add_blog/')
    

