# Generated by Django 2.2 on 2019-09-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0005_auto_20190912_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award_list',
            name='award_image',
            field=models.ImageField(default='award.jpg', upload_to='award_pics'),
        ),
    ]
