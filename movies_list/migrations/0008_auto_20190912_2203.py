# Generated by Django 2.2 on 2019-09-12 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0007_auto_20190912_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cast_list',
            old_name='case_name',
            new_name='cast_name',
        ),
    ]
