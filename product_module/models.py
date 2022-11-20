from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(default='', auto_created=True, verbose_name='عنوان در url')
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
    body =  models.TextField(max_length=500, db_index=True, null=True, verbose_name='توضیحات اصلی محصول')
    designer_word = models.TextField(null=True, blank=True,verbose_name='سخن طراح')
    short_description = models.TextField(max_length=150, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    designer = models.CharField(max_length=300, null=False, blank=False, verbose_name='طراح')
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False, editable=False)
    category = models.ForeignKey('ProductCategory', verbose_name='دسته بندی ها',default='',on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductGallery(models.Model):
    title = models.CharField(default='',verbose_name='نام عکس',max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری محصول'
