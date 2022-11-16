from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(default='', auto_created=True, verbose_name='عنوان در url')
    parent_category = models.ForeignKey('self', blank=True, on_delete=models.CASCADE, null=True,
                                        verbose_name='دسته بندی والد')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=300, null=False)
    slug = models.SlugField(default='', auto_created=True, verbose_name='عنوان در url')
    main_image = models.ImageField(upload_to='images/product/%Y/%m/%d', null=True, verbose_name='تصویر اصلی محصول',
                                   default='')
    image1 = models.ImageField(upload_to='images/product/%Y/%m/%d', null=True, verbose_name='تصویر 1', default='')
    image2 = models.ImageField(upload_to='images/product/%Y/%m/%d', null=True, verbose_name='تصویر 2', default='')
    image3 = models.ImageField(upload_to='images/product/%Y/%m/%d', null=True, verbose_name='تصویر 3', default='')
    image4 = models.ImageField(upload_to='images/product/%Y/%m/%d', null=True, verbose_name='تصویر 4', default='')
    image5 = models.ImageField(upload_to='images/product/%Y/%m/%d', null=True, verbose_name='تصویر 5', default='')
    body = models.TextField(null=False, blank=False)
    short_description = models.CharField(max_length=150, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    designer = models.CharField(max_length=300, null=False, blank=False,verbose_name='طراح')
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False, editable=False)
    category = models.ManyToManyField('ProductCategory', verbose_name='دسته بندی ها')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
