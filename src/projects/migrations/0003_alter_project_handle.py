# Generated by Django 4.2.13 on 2024-05-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='handle',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
