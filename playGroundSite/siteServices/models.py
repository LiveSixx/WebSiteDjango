from django.db import models

from django.utils import timezone

class SiteService(models.Model):
    service_item_title = models.CharField('Название услуги', max_length=50)
    service_item_text_title = models.TextField('Описание на главной странице', max_length=150)
    service_item_text = models.TextField('Полное описание услуги', max_length=1000, default='Отсутствует')
    service_item_price = models.CharField('Стоимость услуги', max_length=50, default='Отсутствует')
    service_item_additional_info = models.TextField('Дополнительная информация', max_length=50, default='Отсутствует')
    service_item_date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):
        return self.service_item_title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
