from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog



def read(request : HttpRequest):

    blogs=Blog.objects.all()

    return render(request, "blogs/read.html", {"blogs" : blogs})




def add(request : HttpRequest):
    if request.method=="POST":
        new_blog=Blog(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'],category=request.POST['category'], poster=request.FILES['poster'])
        
        new_blog.save()
        return redirect("blogs:read")
    
    return render(request,'blogs/add.html', {"categories" : Blog.categories})


def detail(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, "blogs/detail.html", {"blog" : blog})



def update(request : HttpRequest,blog_id):
    blog=Blog.objects.get(id=blog_id)
    if request.method=="POST":
        blog.title=request.POST['title']
        blog.content=request.POST['content']
        blog.is_published=request.POST['is_published']
        blog.published_at= request.POST["published_at"]
        blog.category=request.POST['category']
        blog.save()
        return redirect('blogs:detail',blog_id=blog.id)
    return render(request,'blogs/update.html',{"blog" : blog,'categories':Blog.categories})


def delete(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blogs:read")


def search(request: HttpRequest):
    if 'search' in request.GET:
        query = request.GET['search']
        blog = Blog.objects.filter(title__icontains=query)
    else:
         blog = Blog.objects.all()   
    return render(request, 'blogs/search.html',  {"blog" : blog})




def BlogsCat(request : HttpRequest):

    if "category" in request.GET and request.GET["category"] =="Makeup":
      blogs = Blog.objects.filter(category__contains ="Makeup")

    elif "category" in request.GET and request.GET["category"] =="Movie":
        blogs = Blog.objects.filter(category__contains ="Movie")

    elif "category" in request.GET and request.GET["category"] =="Celebrities":
        blogs = Blog.objects.filter(category__contains ="Celebrities")

    elif "category" in request.GET and request.GET["category"] =="Care":
        blogs = Blog.objects.filter(category__contains ="Care")

    elif "category" in request.GET and request.GET["category"] =="Places":
        blogs = Blog.objects.filter(category__contains ="Places")    
    else:
        blogs = Blog.objects.all()
    return render(request ,"blogs/read.html" , {"blogs" : blogs})

