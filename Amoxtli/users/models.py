from django.db import models
from django.contrib.auth.models import User
from store.models import Book
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, verbose_name = 'Nombre Completo')
    university = models.CharField(max_length = 200, verbose_name = 'Universidad')
    city = models.CharField(max_length = 200, verbose_name = 'Ciudad')
    #wishedBooks = models.ManyToManyField("Book",blank=True,verbose_name='Libros Deseados',related_name="WishedBooks")
    #postedBooks = models.ManyToManyField("Book", blank=True, verbose_name="Libros Publicados", related_name="PostedBooks")
    postalCode = models.IntegerField(default=0, verbose_name='Código Postal')
    colonia = models.CharField(default="", max_length=100, verbose_name = 'Colonia')
    calle = models.CharField(default="", max_length=100, verbose_name = 'Calle')
    numero = models.IntegerField(default=0, verbose_name='Número')
    cardType = models.CharField(default="", max_length=15, verbose_name = 'Empresa (Ej.VISA)')
    cardNumber = models.IntegerField(default=0, verbose_name='Número de Tarjeta')
    cardBack = models.IntegerField(default=0, verbose_name='CVV/CVC')
    cardDate = models.DateField(null=True, verbose_name='Fecha de Vencimiento')
    cardName = models.CharField(default="", max_length=80, verbose_name = 'Nombre del Titular')

    def __str__(self):
        return f'{self.user}'

