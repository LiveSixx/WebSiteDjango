# Generated by Django 3.0.5 on 2020-05-29 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteServices', '0002_auto_20200529_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='SiteService',
        ),
    ]
