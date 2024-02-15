from django.shortcuts import render
from django.http import HttpResponse

class IndexPage:
    @staticmethod
    def as_view(request):
        return HttpResponse("<h1>Test</h1>")
    
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