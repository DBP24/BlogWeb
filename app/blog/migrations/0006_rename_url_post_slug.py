# Generated by Django 5.0.6 on 2024-06-29 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_titulo_post_title_alter_post_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='url',
            new_name='slug',
        ),
    ]
