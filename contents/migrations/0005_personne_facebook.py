# Generated by Django 5.0.4 on 2024-06-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_personne_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]