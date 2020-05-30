from django.db import models
from django.utils.translation import gettext_lazy as _

class Advantage(models.Model):
    
    class Icon(models.TextChoices):
        MAN_TIE = 'fas fa-user-tie fa-10x', _('Человек и галстук ')
        DOLLAR_SIGN = 'fas fa-dollar-sign fa-10x', _('Доллар')
        PERCENT = 'fas fa-percent fa-10x', _('Процент')
        MONEY_CHECK = 'fas fa-money-check-alt fa-10x', _('Кредитная карта')

    advantage_item_title_home_page = models.CharField('Название', max_length=50)
    advantage_item_text_home_page = models.TextField('Краткое описание', max_length=150)
    advantage_item_icon =models.CharField('Список иконок',
        max_length=30,
        choices=Icon.choices,
        default=Icon.MAN_TIE,
    )

    def __str__(self):
        return self.advantage_item_title_home_page

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

class Snippet(models.Model):
    name = models.CharField('Имя', max_length=45)
    phone = models.CharField('Телефон', max_length=45)
    body = models.TextField('Текст сообщения', max_length=250)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения по обратной связи'
    

    def __str__(self):
        return self.name

