# Generated by Django 4.0.2 on 2022-02-17 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_publicacion_delete_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publicacion',
            new_name='Post',
        ),
    ]
