# Generated by Django 2.2.7 on 2020-11-24 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCommandes', '0005_auto_20201123_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='AppCommandes.Categorie'),
            preserve_default=False,
        ),
    ]
