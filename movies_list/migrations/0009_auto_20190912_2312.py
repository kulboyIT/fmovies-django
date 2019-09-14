# Generated by Django 2.2 on 2019-09-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('movies_list', '0008_auto_20190912_2203'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Server_type_list',
            new_name='Content_type_list',
        ),
        migrations.AlterModelOptions(
            name='content_type_list',
            options={'verbose_name_plural': 'content_type'},
        ),
        migrations.RenameField(
            model_name='content_type_list',
            old_name='server_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='link_list',
            old_name='server_type',
            new_name='link_type',
        ),
        migrations.AlterField(
            model_name='language_list',
            name='language_short_code',
            field=models.CharField(max_length=5),
        ),
    ]