# Generated by Django 3.0.1 on 2020-10-19 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.CharField(blank=True, max_length=100, null=True)),
                ('BrandTitle', models.CharField(blank=True, max_length=80, null=True)),
                ('BrandCateory', models.CharField(blank=True, default='Shopping', max_length=200, null=True)),
                ('BrandSlug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('BrandLogo', models.ImageField(blank=True, null=True, unique=True, upload_to='Brand-Images')),
                ('BrandDescription', models.CharField(blank=True, max_length=170, null=True)),
                ('BrandKeywords', models.CharField(blank=True, max_length=500, null=True)),
                ('BrandAddedDateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'db_table': 'brandsModel',
                'ordering': ('BrandName',),
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(blank=True, max_length=70, null=True)),
                ('CategorySlug', models.SlugField(max_length=100, unique=True)),
                ('CategoryDescription', models.CharField(blank=True, max_length=250, null=True)),
                ('CategoryAddedDateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
                'ordering': ('CategoryName',),
            },
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(blank=True, max_length=80, null=True)),
                ('MessageTitle', models.CharField(blank=True, max_length=200, null=True)),
                ('Department', models.CharField(blank=True, max_length=50, null=True)),
                ('EmailAddress', models.EmailField(blank=True, max_length=254, null=True)),
                ('Message', models.CharField(blank=True, max_length=800, null=True)),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'contactUsModel',
            },
        ),
        migrations.CreateModel(
            name='NewsletterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'newsletter',
                'verbose_name_plural': 'newsletters',
                'db_table': 'newslettermodel',
                'ordering': ('Email',),
            },
        ),
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=80, null=True)),
                ('Message', models.CharField(blank=True, max_length=800, null=True)),
                ('Status', models.CharField(blank=True, default='Active', max_length=50, null=True)),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
                'db_table': 'notificationModel',
                'ordering': ('Title',),
            },
        ),
        migrations.CreateModel(
            name='CouponProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CouponProductImage', models.ImageField(default='Product-Images/default.png', unique=True, upload_to='Product-Images')),
                ('CouponProductTitle', models.CharField(blank=True, max_length=70, null=True)),
                ('CouponProductDescription', models.CharField(blank=True, max_length=800, null=True)),
                ('CouponProductKeywords', models.CharField(blank=True, max_length=500, null=True)),
                ('CouponProductSlug', models.SlugField(max_length=200, unique=True)),
                ('CouponCode', models.CharField(blank=True, max_length=500, null=True)),
                ('CouponLink', models.URLField(blank=True, max_length=500, null=True)),
                ('CouponProductPrice', models.IntegerField(blank=True, default=10, null=True)),
                ('CouponProductDisplayPrice', models.IntegerField(blank=True, default=20, null=True)),
                ('CouponProductRating', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('CouponProductTotalRating', models.IntegerField(blank=True, null=True)),
                ('CouponStatus', models.CharField(blank=True, default='Active', max_length=100, null=True)),
                ('CouponVerified', models.BooleanField(default=True)),
                ('CouponProductAddedDateTime', models.DateTimeField(auto_now_add=True)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='administrationsection.BrandsModel')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='administrationsection.Categories')),
            ],
            options={
                'db_table': 'couponProducts',
            },
        ),
    ]
