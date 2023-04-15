from django.db import models

# Create your models here.

# Model for contact us messages
class ContactUsModel(models.Model):
    FullName = models.CharField(max_length=80,null=True,blank=True)
    MessageTitle = models.CharField(max_length=200,null=True,blank=True)
    Department = models.CharField(max_length=50, null=True,blank=True)
    EmailAddress = models.EmailField(blank=True,null=True)
    Message = models.CharField(max_length=800,null=True,blank=True)
    DateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contactUsModel"


# Model for notifications
class NotificationModel(models.Model):
    Title = models.CharField(max_length=80,null=True,blank=True)
    Message = models.CharField(max_length=800,null=True,blank=True)
    Status = models.CharField(max_length=50,null=True,blank=True,default="Active")
    DateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notificationModel"
        ordering = ("Title",)
        verbose_name = "notification"
        verbose_name_plural = "notifications"

    def __str__(self):
        return self.Title

# News letter model
class NewsletterModel(models.Model):
    Email = models.EmailField(blank=True,null=True)

    class Meta:
        db_table = 'newslettermodel'
        ordering = ("Email",)
        verbose_name = "newsletter"
        verbose_name_plural = "newsletters"

    def __str__(self):
        return self.Email


# Model for brands
class BrandsModel(models.Model):
    BrandName = models.CharField(max_length=100,blank=True,null=True)
    BrandTitle = models.CharField(max_length=80,null=True,blank=True)
    BrandCateory = models.CharField(max_length=200,null=True,blank=True,default='Shopping')
    BrandSlug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    BrandLogo = models.ImageField(upload_to="Brand-Images",unique=True,blank=True,null=True)
    BrandDescription = models.CharField(max_length=170,blank=True,null=True)
    BrandKeywords = models.CharField(max_length=500,blank=True,null=True)
    BrandAddedDateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "brandsModel"
        ordering = ("BrandName",)
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def __str__(self):
        return self.BrandName

    def get_absolute_url(self):
        return f"/{self.BrandSlug}/coupon-codes/"



# Categories model
class Categories(models.Model):
    CategoryName = models.CharField(max_length=70,blank=True,null=True)
    CategorySlug = models.SlugField(max_length=100,unique=True)
    CategoryDescription = models.CharField(max_length=250,blank=True,null=True)
    CategoryAddedDateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"
        ordering = ("CategoryName",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.CategoryName


# Coupon products model
class CouponProducts(models.Model):
    Brand = models.ForeignKey(BrandsModel,related_name="brand",on_delete=models.CASCADE)
    Category = models.ForeignKey(Categories,related_name="category",on_delete=models.CASCADE)
    CouponProductImage = models.ImageField(upload_to="Product-Images",unique=True,default='Product-Images/default.png')
    CouponProductTitle = models.CharField(max_length=70,blank=True,null=True)
    CouponProductDescription = models.CharField(max_length=800,blank=True,null=True)
    CouponProductKeywords = models.CharField(max_length=500,blank=True,null=True)
    CouponProductSlug = models.SlugField(max_length=200,unique=True)
    CouponCode = models.CharField(max_length=500,blank=True,null=True)
    CouponLink = models.URLField(max_length=500,blank=True,null=True)
    CouponProductPrice = models.IntegerField(blank=True,null=True,default=10)
    CouponProductDisplayPrice = models.IntegerField(blank=True,null=True,default=20)
    CouponProductRating = models.DecimalField(blank=True,null=True,max_digits=4,decimal_places=1)
    CouponProductTotalRating = models.IntegerField(blank=True,null=True)
    CouponStatus = models.CharField(max_length=100,blank=True,null=True,default="Active")
    CouponVerified = models.BooleanField(default=True)
    CouponProductAddedDateTime = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "couponProducts"
        
    
    
    def __str__(self):
        return self.CouponProductTitle


    # Function for deleting coupon product image
    def delete(self,*args,**kwargs):
        self.CouponProductImage.delete()
        super().delete(*args,**kwargs)

    
    def get_absolute_url(self):
        return f"/coupon-code/{self.CouponProductSlug}/"




