from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import random




# Create your models here.


class Genre(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    name = models.CharField(max_length = 100, verbose_name = 'Género')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:store-genres-detail', args=[self.slug])

class Subject(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    name = models.CharField(max_length = 100, verbose_name = 'Materia')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:store-subjects-detail', args=[self.slug])


class Book(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    title = models.CharField(max_length = 200, verbose_name = 'Título')
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    author = models.CharField(max_length = 200,  verbose_name = 'Autor')
    publisher = models.CharField(max_length = 200, verbose_name = 'Editorial')
    description = models.CharField(max_length=500, blank=True,verbose_name='Descripción')
    datePosted = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Publicación')
    publishedBy = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Publicado por')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Género')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Materia')
    rating = models.PositiveIntegerField(default=0,verbose_name='Calificación')
    quality = models.CharField(max_length = 100, verbose_name = 'Calidad')
    image = models.ImageField(default='default-book.png', upload_to='book_pics')

    class Meta:
        ordering = ('title', )
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:store-detail', kwargs={'pk':self.pk})
    
    def getOldPrice(self):
        ran = random.randint(50, 200)
        ran2 = random.randint(10, 50)
        if((self.price-200) <= 0):
            return self.price + ran2
        else:
            return self.price + ran




