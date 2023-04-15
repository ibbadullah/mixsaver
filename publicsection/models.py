from django.db import models
from ckeditor.fields import RichTextField


class UsersSearchQueriesModel(models.Model):
    userQuery = models.CharField(max_length=500,blank=True,null=True)
    category = models.CharField(max_length=200,blank=True,null=True)
    userIp = models.CharField(max_length=200,blank=True,null=True)
    userEmail = models.EmailField(blank=True,null=True)

    class Meta:
        db_table = "usersqueriesmodel"


# Model for articles
class ArticlesModel(models.Model):
    ArticleTitle = models.CharField(max_length=60,null=True,blank=True)
    ArticleBodyText = RichTextField(null=True,blank=True)
    ArticleImage = models.ImageField(upload_to="ArticleImages",null=True,blank=True)
    ArticleKeywords = models.CharField(max_length=500,null=True,blank=True)
    ArticleSlug = models.SlugField(max_length=255,unique=True)
    ArticlePublishedDate = models.DateTimeField(auto_now_add=True)
    ArticleUpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "articlesmodel"
        ordering = ('ArticleTitle',)

    def __str__(self):
        return self.ArticleTitle

    def get_absolute_url(self):
        return f"/article/{self.ArticleSlug}/"

