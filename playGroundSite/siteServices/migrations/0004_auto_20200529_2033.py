# Generated by Django 3.0.5 on 2020-05-29 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteServices', '0003_auto_20200529_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteservice',
            name='service_item_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='siteservice',
            name='service_item_additional_info',
            field=models.TextField(default='Отсутствует', max_length=50, verbose_name='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='siteservice',
            name='service_item_text',
            field=models.TextField(max_length=1000, verbose_name='Полное описание услуги'),
        ),
    ]
