# Generated by Django 2.2 on 2019-09-12 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0006_auto_20190912_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cast_list',
            old_name='cast_iamge',
            new_name='cast_image',
        ),
    ]