from django.contrib import admin
from .models import Node

class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'symbol', 'name', 'url', 'parent', 'related_menu']
    list_editable = ['name', 'symbol', 'parent', 'url', 'related_menu']
    list_display_links = ['id']
    

admin.site.register(Node, NodeAdmin)
