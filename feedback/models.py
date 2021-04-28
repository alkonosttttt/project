from django.db import models


class Feedback(models.Model):
    fio = models.CharField('ФИО', max_length=130)
    city = models.CharField('Город', max_length=100, blank=True)
    phone = models.CharField("Телефон", max_length=25)

    gender = models.IntegerField("Пол", choices=[(1, 'Мужской'), (2, 'Женский')], default=1)


    service = models.IntegerField('О какой услуге Вы хотите оставить отзыв?',
                                  choices=((1, 'Покупка квартиры'),
                                           (2, 'Работа персонала'),
                                           (3, 'Использование сайта'),
                                           (4, 'Прочее')), default=1)

    text = models.TextField("Отзыв")

    notice = models.BooleanField('Получать новости о новых предложениях на электронную почту?', default=False)
    email = models.EmailField("E-Mail", max_length=130)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв от {self.fio}"
