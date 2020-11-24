from AppCommandes.models import *
from django.db import transaction
import random

categorie = Categorie.objects.all()

with transaction.atomic():
    for cat in categorie:
        nbProduit = random.randint(10, 110)
        alleeM = AlleeMagasin.objects.filter(categorie=cat)
        alleeR = AlleeReserve.objects.filter(categorie=cat)
        for i in range(2, nbProduit):
            prod = Produit(
                name="Produit" + str(i),
                price=round(random.uniform(2, 20), 2),
                stock=random.randint(5, 300),
                alleeMagasin=alleeM[random.randint(0, len(alleeM) - 1)],
                alleeReserve=alleeR[random.randint(0, len(alleeR) - 1)],
            )
            prod.save()
