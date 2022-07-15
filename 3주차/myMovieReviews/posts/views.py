from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        release = request.POST["release"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        grade = request.POST["grade"]
        running_time = request.POST["running_time"]
        content = request.POST["content"]

        Post.objects.create(title=title, release=release, director=director, actor=actor, genre=genre, grade=grade, running_time=running_time, content=content )

        return redirect("/")

    context = {}
    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        grade = request.POST["grade"]
        running_time = request.POST["running_time"]
        content = request.POST["content"]

        Post.objects.filter(id=id).update(title=title, release=release, director=director, actor=actor, genre=genre, grade=grade, running_time=running_time, content=content )

        return redirect(f"/post/{id}")

    elif request.method == "GET":
        post = Post.objects.get(id=id)
        context = {
            "post": post
        }
        return render(request, template_name="posts/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")