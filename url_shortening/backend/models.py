from django.db import models
from hashlib import md5


class Link(models.Model):
    long_link = models.URLField(verbose_name='Ссылка')
    short_link = models.SlugField(verbose_name='Сокращенная ссылка')
    number_clicks = models.IntegerField(default=0, verbose_name='Число переходов')

    class Meta:
        verbose_name = u'Ссылка'
        verbose_name_plural = u'Ссылки'

    def clicked(self):
        self.number_clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.short_link = md5(self.long_link.encode()).hexdigest()[:4]

        return super().save(*args, **kwargs)