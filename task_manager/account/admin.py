from django.contrib import admin
from account.models import *

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
  list_display = [ 'id', 'birth_date', 'gender']
admin.site.register(UserAccount, UserAccountAdmin)