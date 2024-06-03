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
    classe_keys = ["Clasa a V-a", "Clasa a VI-a", "Clasa a VII-a",
                   "Clasa a VIII-a", "Clasa a IX-a", "Clasa a X-a",
                   "Clasa a XI-a", "Clasa a XII-a"]
    tag_key = "tag"
    
    @staticmethod
    def as_view(request):
        sorted_posts = Post.objects.order_by("-pub_date")
        years:list[int] = [datetime.now().date().year - i for i in range(8) ]
        
        tags = Tag.objects.all()[:16]
        if request.method == 'POST':
            # Handle the search filter
            if IndexPage.post_name_key in request.POST:
                #filter by name
                search: str = request.POST[IndexPage.post_name_key]
                sorted_posts = list(filter(lambda post: search.lower() in post.title.lower(), sorted_posts))
                IndexPage.context["search"] = search
                
            classes_sorted_posts = []
            flag_classes: bool = False
            for class_key in IndexPage.classe_keys:
                if class_key in request.POST:
                    flag_classes = True
                    for post in sorted_posts:
                        if class_key in map(lambda el: el.name, post.tags.all()):
                            classes_sorted_posts.append(post)
                           
            years_sorted_posts = [] 
            flag_years: bool = False
            for year_key in years:
                if str(year_key) in request.POST:
                    flag_years = True
                    for post in sorted_posts:
                        if post.pub_date.year == year_key:
                            years_sorted_posts.append(post)
                            
            
            if not flag_classes:
                filtered_sorted_posts = years_sorted_posts
            elif not flag_years:
                filtered_sorted_posts = classes_sorted_posts
            else:               
                filtered_sorted_posts = [post for post in classes_sorted_posts
                                              for post_p in years_sorted_posts
                                              if post == post_p]
                            
            print(request.POST.keys())
            print(filtered_sorted_posts, flag_classes, flag_years)
            if flag_classes or flag_years: sorted_posts = list(filtered_sorted_posts)
            
            if IndexPage.tag_key in request.POST:
                tag = request.POST[IndexPage.tag_key]
                filtered_sorted_posts = []
                for post in sorted_posts:
                    print(post.tags.all())
                    if tag in map(lambda tag: tag.name, post.tags.all()):
                        filtered_sorted_posts.append(post)
                sorted_posts = list(filtered_sorted_posts)
        
        last_posts = sorted_posts[:IndexPage.numberOfPosts]
        IndexPage.context["post_list"] = last_posts
        IndexPage.context["tags"] = tags
        IndexPage.context["years"] = years
        return render(request, IndexPage.template_name, IndexPage.context)
    
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