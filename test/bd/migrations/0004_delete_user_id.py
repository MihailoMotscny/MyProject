# Generated by Django 4.1.7 on 2023-04-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0003_user_id_remove_artiles_iduser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_id',
        ),
    ]