# Generated by Django 4.2.13 on 2024-05-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='handle',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
