# Generated by Django 5.1.2 on 2024-12-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_alter_directorgeneral_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
