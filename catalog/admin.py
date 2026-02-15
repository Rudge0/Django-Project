from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import LiteraryFormat, Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list = ["title", "price", "format"]
    search_fields = ["title", ]
    list_display = list
    list_filter = list

@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "pseudonym", "is_staff")
    UserAdmin.fieldsets[1][1]["fields"] = ("first_name", "last_name", "pseudonym", "email")
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("first_name", "last_name", "pseudonym", )}),)

admin.site.register(LiteraryFormat)
