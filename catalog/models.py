import uuid
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название жанра')
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def genre_filter(self):
        return reverse('catalog:genre_filter', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name='Язык')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Слаг')
    authors = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, verbose_name='Описание')
    cover = models.FileField(upload_to='book_cover/%Y/%m/%d/', default='img/no-image.jpg')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book_detail', kwargs={'slug': self.slug})

    def book_delete(self):
        return reverse('stuff:book_delete', kwargs={'pk': self.pk})

    def book_update(self):
        return reverse('stuff:book_update', kwargs={'pk': self.pk})

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique key for this particular key')
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=100, verbose_name='Издательство')
    ISBN = models.CharField('ISBN', max_length=100)
    return_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата книги')

    loan_status = (
        ('m', 'maintains'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=loan_status, default='m', blank=True, help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['return_date']
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляр книг'
        permissions = (('can_mark_returned','Set book as returned'),)

    def __str__(self):
        return '{} {}'.format(self.id, self.book.title)

    @property
    def is_overdue(self):
        if self.return_date and date.today() > self.return_date:
            return True
        return False

    def book_reserved(self):
        update_status = self.status = 'r'
        return update_status


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя автора')
    slug = models.SlugField(max_length=100, verbose_name='Слаг', blank=True)
    photo = models.ImageField(upload_to='author_photo/%Y/%m/%d/', default='img/no-image.jpg', blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True)
    date_of_dead = models.DateField(verbose_name='Дата смерти', blank=True)
    books = models.ManyToManyField(Book, verbose_name='Книги', blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('catalog:author_detail', kwargs={'slug': self.slug})

    def delete_author(self):
        return reverse('stuff:author_delete', kwargs={'slug': self.slug})

    def update_author(self):
        return reverse('stuff:author_update', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
