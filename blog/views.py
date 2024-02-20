from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Post

class IndexPage:
    template_name = "blog/index.html"
    numberOfPosts = 5
    context = {}
    
    @staticmethod
    def as_view(request):
        last_posts = Post.objects.order_by("-pub_date")[:IndexPage.numberOfPosts]
        IndexPage.context["post_list"] = last_posts
        return render(request, IndexPage.template_name, IndexPage.context)
    
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
    template_name = "blog/details.html"
    
    @staticmethod
    def as_view(request, blog_id):
        post = get_object_or_404(Post, pk=blog_id)
        
        return render(request, DetailsPage.template_name, context={"post" : post})