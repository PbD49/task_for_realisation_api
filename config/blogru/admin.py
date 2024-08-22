from django.contrib import admin
from .models import Blog, User


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ('user_id', 'title', 'content')
    list_display = ('title', 'content', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('user_id', 'time_create')
    ordering = ('time_create', )
    list_per_page = 5
    actions = ('withdraw_from_publication', 'put_it_on_publication')

    @admin.action(description='Снять с публикации выбранные записи')
    def withdraw_from_publication(self, request, queryset):
        queryset.update(is_published=False)
        self.message_user(request, f"Выбранные записи сняты с публикации ({queryset.count()} шт.)")

    @admin.action(description='Опубликовать выбранные записи')
    def put_it_on_publication(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, f'Выбранные записи будут опубликованы ({queryset.count()}) шт.')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
