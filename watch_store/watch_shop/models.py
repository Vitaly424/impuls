from django.db import models


class Brand(models.Model):

    slug_brand = models.SlugField(verbose_name='URL бренда', max_length=255, unique=True, db_index=True)
    title_brand = models.CharField(verbose_name='Название бренда', max_length=50, )
    description_brand = models.TextField(verbose_name='Описание бренда', blank=True)
    created_brand_at = models.DateTimeField(verbose_name='Дата добавления бренда', auto_now_add=True)
    updated_brand_at = models.DateTimeField(verbose_name='Дата обновления бренда', auto_now=True)
    logo_brand = models.ImageField(verbose_name='Картинка бренда', upload_to='photos/brands/%Y/%m/%d/', blank=True)
    hidden_brand = models.BooleanField(verbose_name='Скрытый бренд', default=False)
    country_brand = models.CharField(verbose_name='Страна бренда', max_length=50)

    def __str__(self):
        return self.title_brand

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['title_brand']


class SubBrand(models.Model):

    slug_subbrand = models.SlugField(verbose_name='URL подбренда', max_length=255, unique=True, db_index=True)
    title_subbrand = models.CharField(verbose_name='Название подбренда', max_length=100)
    description_subbrand = models.TextField(verbose_name='Описание подбренда', blank=True)
    created_subbrand_at = models.DateTimeField(verbose_name='Дата добавления подбренда', auto_now_add=True)
    updated_subbrand_at = models.DateTimeField(verbose_name='Дата обновления подбренда', auto_now=True)
    logo_subbrand = models.ImageField(verbose_name='Картинка подбренда', upload_to='photos/subbrands/%Y/%m/%d/', blank=True)
    hidden_subbrand = models.BooleanField(verbose_name='Скрытый подбренд', default=False)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Бренд', related_name='subbrands')

    def __str__(self):
        return self.title_subbrand

    class Meta:
        verbose_name = 'Подбренд'
        verbose_name_plural = 'Подбренды'
        ordering = ['title_subbrand']


class Product(models.Model):

    vendor_code = models.CharField(verbose_name='Артикул продукта', max_length=50, unique=True, db_index=True)
    title_product = models.CharField(verbose_name='Название продукта', max_length=100)
    description_product = models.TextField(verbose_name='Описание продукта', )
    created_product_at = models.DateTimeField(verbose_name='Дата добавления продукта', auto_now_add=True)
    updated_product_at = models.DateTimeField(verbose_name='Дата обновления продукта', auto_now=True)
    main_logo_product = models.ImageField(verbose_name='Главная картинка продукта', upload_to='photos/products/%Y/%m/%d/', blank=True)
    price_product = models.DecimalField(verbose_name='Цена продукта', max_digits=10, decimal_places=2)
    hidden_product = models.BooleanField(verbose_name='Скрытый продукт', default=False)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Бренд', related_name='products')
    subbrand = models.ForeignKey('SubBrand', on_delete=models.PROTECT, verbose_name='Подбренд', blank=True, related_name='products')

    def __str__(self):
        return self.title_product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title_product']


class ImagesProduct(models.Model):
    id_product = models.ForeignKey('Product', on_delete=models.CASCADE, default=None, related_name='images_product')
    products_image_other = models.ImageField(upload_to='photos/products/%Y/%m/%d', blank=True)


