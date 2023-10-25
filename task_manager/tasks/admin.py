from django.contrib import admin
from tasks.models import *
# Register your models here.
class priorityAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']

class TaskAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'created_at', 'due_date']
  

class PhotoAdmin(admin.ModelAdmin):
  list_display = [ 'id', 'task']

admin.site.register(Priority, priorityAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(multiplePhoto, PhotoAdmin)


