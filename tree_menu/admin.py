from django.contrib import admin
from .models import Node

class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'parent']
    list_editable = ['name', 'parent', 'url']
    list_display_links = ['id']
    

admin.site.register(Node, NodeAdmin)
