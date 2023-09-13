from django.contrib import admin
from api_triunfo.users.models import User
# Register your models here.

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(User)
