# Generated by Django 3.1.4 on 2021-09-30 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_recipe_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cidade',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
    ]