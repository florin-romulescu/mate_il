from django.contrib import admin
from .models import Post, Tag, Attachment

class AdminSite(admin.AdminSite):
    site_title = "MATE IL"

admin_site = AdminSite(name="mate_il")

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Post Information", {"fields" : ["title", "author", "description", "pub_date", "image"]}),
        ("Tags", {"fields" : ["tags"], "classes" : ["collapse"]}),
        ("Attachments", {"fields" : ["attachments"], "classes" : ["collapse"]})
    ]

# Register your models here.
admin_site.register(Post, PostAdmin)
admin_site.register(Tag)
admin_site.register(Attachment)