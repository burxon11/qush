from django.contrib import admin

from menyu.models import Menyu, Category, Comment

# Register your models here.


admin.site.register(Menyu)
admin.site.register(Category)
admin.site.register(Comment)