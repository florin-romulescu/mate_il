from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Post

class IndexPage:
    @staticmethod
    def as_view(request):
        return render(request, "blog/index.html")
    
class WorksheetPage:
    @staticmethod
    def as_view(request):
        return HttpResponse("<h1>Worksheet</h1>")
    
class ExercisesPage:
    @staticmethod
    def as_view(request):
        return HttpResponse("<h1>Exercises</h1>")
    
class BlogPage:
    @staticmethod
    def as_view(request):
        return HttpResponse("<h1>Blog</h1>")
    
class DetailsPage:
    @staticmethod
    def as_view(request, blog_id):
        post = get_object_or_404(Post, pk=blog_id)
        
        return render(request, "blog/details.html", context={"post" : post})