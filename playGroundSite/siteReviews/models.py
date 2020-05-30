from django.db import models

from django.utils import timezone

class SnippetReview(models.Model):
    name_review = models.CharField('Имя', max_length=45)
    email_review = models.CharField('Почта', max_length=45)
    body_review = models.TextField('Текст отзыва', max_length=400)
    time_pub_review = models.DateTimeField('Дата отзыва',default=timezone.now)


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    

    def __str__(self):
        return self.name_review
