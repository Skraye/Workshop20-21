from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.db.models.signals import post_save


class Commande(models.Model):
    """
        Classe représentant la commande
        - Le code commande est généré aléatoirement
        à la création de la commande
        - Les dates sont gérés automatiquement
        - Le statut commande est un chiffre représentant
            un état
            0 = WAITING
            1 = IN_PROGRESS
            2 = CONFIRM
            3 = FINISH
    """

    codeCommande = models.CharField(max_length=128, primary_key=True)
    dateCreation = models.DateTimeField(default=datetime.now)
    dateModification = models.DateTimeField(auto_now=True)
    statutCommande = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)]
    )

    def __str__(self):
        return self.codeCommande


class HistoryAction(models.Model):
    """
        Historique des actions effectués sur les commandes
        Avec le type,la date et l'auteur
    """

    modificationType = models.CharField(max_length=64)
    modificationDate = models.DateTimeField(auto_now=True)
    modificationBy = models.CharField(max_length=128)
    commande = models.ForeignKey(
        Commande, on_delete=models.CASCADE, related_name="commande"
    )

    def __str__(self):
        return self.modificationType


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
    versionFront = models.CharField(max_length=64)
    versionBackend = models.CharField(max_length=64)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mailSupport

