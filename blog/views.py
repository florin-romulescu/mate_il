from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from datetime import datetime

from .models import Post
from .models import Tag

import io, zipfile

class IndexPage:
    template_name = "blog/index.html"
    numberOfPosts = 5
    context = {}
    
    post_name_key = "search-bar"
    tag_key = "tag"
    
    @staticmethod
    def as_view(request):
        sorted_posts = Post.objects.order_by("-pub_date")
        last_posts = sorted_posts[:IndexPage.numberOfPosts]
        
        tags = Tag.objects.all()[:16]
        if request.method == 'POST':
            # Handle the search filter
            if IndexPage.post_name_key in request.POST:
                #filter by name
                search: str = request.POST[IndexPage.post_name_key]
                last_posts = filter(lambda post: search.lower() in post.title.lower(), last_posts)
                IndexPage.context["search"] = search
                
            if IndexPage.tag_key in request.POST:
                #filter by tags
                pass
        
        IndexPage.context["post_list"] = last_posts
        IndexPage.context["tags"] = tags
        IndexPage.context["years"] = [datetime.now().date().year - i for i in range(8) ]
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
    
def download_attachment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.attachments.all():
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
            for attachment in post.attachments.all():
                with attachment.file.open('rb') as file:
                    zip_file.writestr(attachment.file.name, file.read())
                    
        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{post.title}_attachments.zip"'
        return response
    
    return HttpResponse("This post has no attachment.")