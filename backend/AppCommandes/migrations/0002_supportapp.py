# Generated by Django 2.2.7 on 2019-11-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCommandes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailSupport', models.CharField(max_length=64)),
                ('versionFront', models.CharField(max_length=64)),
                ('versionBackend', models.CharField(max_length=64)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
