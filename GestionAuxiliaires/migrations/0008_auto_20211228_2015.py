# Generated by Django 3.2.9 on 2021-12-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAuxiliaires', '0007_alter_person_sexe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitfin',
            old_name='periode',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='person',
            name='sexe',
            field=models.CharField(choices=[('F', 'Feminin'), ('M', 'Masculin')], max_length=1),
        ),
    ]
