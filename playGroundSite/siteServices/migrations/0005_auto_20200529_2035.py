# Generated by Django 3.0.5 on 2020-05-29 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteServices', '0004_auto_20200529_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteservice',
            name='service_item_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
