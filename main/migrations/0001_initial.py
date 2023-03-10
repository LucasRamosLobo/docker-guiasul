# Generated by Django 3.1.4 on 2021-09-29 15:55

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.CharField(max_length=400)),
                ('descricao', models.TextField()),
                ('endereco', models.TextField()),
                ('servicos', models.TextField()),
                ('detalhes', models.CharField(max_length=5)),
                ('desde', models.CharField(max_length=5)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.topic')),
            ],
        ),
    ]
