from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "TodoList Admin"
admin.site.index_title ="Welcome Kafoo"
admin.site.site_title = "TodoList"

class TodoListAdmin(admin.ModelAdmin):
     list_display = ("user", "item", "description", "iscompleted", "datetime")
     


admin.site.register(Todolist, TodoListAdmin)

