from django.contrib import admin
from .models import ArticlesModel
# Register your models here.

class ArticlesCustomization(admin.ModelAdmin):
    prepopulated_fields = {'ArticleSlug':('ArticleTitle',)}


admin.site.register(ArticlesModel,ArticlesCustomization)
