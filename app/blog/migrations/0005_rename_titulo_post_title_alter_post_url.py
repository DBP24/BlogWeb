# Generated by Django 5.0.6 on 2024-06-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Titulo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(max_length=250, verbose_name='Slug URL'),
        ),
    ]
