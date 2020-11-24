from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.db.models.signals import post_save


class Magasin(models.Model):

    ville = models.CharField(max_length=128)
    codePostal = models.IntegerField()

    def __str__(self):
        return self.ville


class Role(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Categorie(models.Model):

    name = models.CharField(max_length=64)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name


class AlleeReserve(models.Model):

    number = models.IntegerField()
    floor = models.IntegerField()
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="alleereserves"
    )

    def __str__(self):
        return str(self.number)


class AlleeMagasin(models.Model):

    number = models.IntegerField()
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="alleemagasins"
    )

    def __str__(self):
        return str(self.number)


class Produit(models.Model):

    name = models.CharField(max_length=64)
    price = models.IntegerField()
    stock = models.FloatField()
    alleeMagasin = models.ForeignKey(
        AlleeMagasin, on_delete=models.CASCADE, related_name="produits"
    )
    alleeReserve = models.ForeignKey(
        AlleeReserve, on_delete=models.CASCADE, related_name="produits"
    )
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="produits"
    )

    def __str__(self):
        return self.name


class Alerte(models.Model):
    codeProblems = models.CharField(max_length=4)
    produit = models.ForeignKey(
        Produit, on_delete=models.CASCADE, related_name="alerte", null=True
    )
    alleeMagasin = models.ForeignKey(
        AlleeMagasin, on_delete=models.CASCADE, related_name="alerte", null=True
    )


class HistoryLogin(models.Model):
    """
        Historique des connexions effectués par 
        les utilisateurs
    """

    mail = models.CharField(max_length=64)
    loginDate = models.DateTimeField(default=datetime.now)
    ipAddress = models.CharField(max_length=64, null=True)


class SupportApp(models.Model):
    """
        Contact support et version de l'application
    """

    mailSupport = models.CharField(max_length=64)
    numSupport = models.CharField(max_length=32)
    versionBackend = models.CharField(max_length=64)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mailSupport

