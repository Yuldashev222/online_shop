from django.contrib import admin

from .models import MainCategory, SubCategory
from apps.general.models import Banner


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    prepopulated_fields = {'slug': ['name_uz']}


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'slug', 'image')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name_uz']}
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_category', 'name_uz', 'slug', 'name_ru')
    list_filter = ['main_category']
    search_fields = ['name_uz']
    list_editable = ('name_uz',)
    search_help_text = 'search with name'
    prepopulated_fields = {'slug': ['name_uz']}


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_category', 'title_uz', 'slug', 'title_ru', 'desc_uz',
                    'desc_ru')
    prepopulated_fields = {'slug': ['title_uz']}