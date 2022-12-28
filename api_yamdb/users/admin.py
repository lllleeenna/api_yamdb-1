from django.contrib import admin

from .models import User
#from review.models import (Category, Genre,
#                           Title, Review, Comment)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'bio', 'role')
    search_fields = ('username','email')
    list_filter = ('role',)
    empty_value_display = '-пусто-'

admin.site.register(User, UserAdmin)
#admin.site.register(Category)
#admin.site.register(Genre)
#admin.site.register(Title)
#admin.site.register(Review)
#admin.site.register(Comment)
