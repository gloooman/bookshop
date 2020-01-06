from django.db import models
from django.shortcuts import reverse
from exclusivebooleanfield import ExclusiveBooleanField
from django.utils.text import slugify
from time import time


# def gen_slug(s):
#     new_slug = slugify(s, allow_unicode=True)
#     return new_slug+str(int(time()))


class Genre(models.Model):
    genre_name = models.CharField('Жанр', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # slug = models.SlugField(max_length=250, blank=True, unique=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.genre_name)
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre_name

    def get_absolute_url(self):
        return reverse('genre_detail_url', kwargs={'id': self.id})


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)
    foto = models.ImageField(upload_to='static/media/author_images/',
                             default='static/media/author_images/placeholder.png')
    author_review = models.TextField('Рецензия', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # slug = models.SlugField(max_length=250, blank=True, unique=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(f"{self.first_name} {self.last_name}")
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Автор"
        verbose_name_plural = "Автора"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('author_detail_url', kwargs={'id': self.id})

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


class Language(models.Model):
    language = models.CharField('Язык', max_length=200, blank=True, default='')
    # slug = models.SlugField(max_length=250, blank=True, unique=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.language)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Язык книги"
        verbose_name_plural = "Языки книги"

    def get_absolute_url(self):
        return reverse('language_detail_url', kwargs={'id': self.id})


class CountryOfOrigin(models.Model):
    country = models.CharField('Cтрана написания', max_length=200)
    # slug = models.SlugField(max_length=250, blank=True, unique=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.country)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Стана производства"
        verbose_name_plural = "Страны производства"

    def get_absolute_url(self):
        return reverse('country_detail_url', kwargs={'id': self.id})


class Product(models.Model):
    name = models.CharField('Название книги', max_length=200)
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.DO_NOTHING)
    country = models.ForeignKey(CountryOfOrigin, verbose_name='Cтрана написания', on_delete=models.DO_NOTHING, blank=True)
    price = models.DecimalField('Цена', default=0, decimal_places=2, max_digits=15)
    genre = models.ManyToManyField(Genre)
    review = models.TextField('Рецензия', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # slug = models.SlugField(max_length=250, blank=True, unique=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.name)
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.name} ({self.author.__str__()})"

    def get_main_image_url(self):
        main_image = self.productimage_set.get(is_main=True)
        return main_image.image.url

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'id': self.id})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/media/products_images/', blank=False)
    is_active = models.BooleanField(default=True)
    is_main = ExclusiveBooleanField(default=False, on=('product',))
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'картинка {self.product} id={self.id}'

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"



