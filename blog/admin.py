from django.contrib import admin
from .models import Publication, Comment


class CommentList(admin.StackedInline):
    extra = 0
    model = Comment
    readonly_fields = ("date", )
    fieldsets = ((None, {'fields': ('user', 'text', 'date')}),)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    inlines = [CommentList]
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'slug')}),
        ("Основная информация", {'fields': ('author', 'short_text', 'description', 'image')}),
    )
