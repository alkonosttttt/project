from django.db import models
from django.utils import timezone

from account.models import User


class Publication(models.Model):
    title = models.CharField("Заголовок", max_length=130)
    slug = models.SlugField("URL публикации")
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, related_name="post")
    description = models.TextField('Текст публикации', blank=True)
    short_text = models.TextField('Краткое описание', blank=True, max_length=400,
                                        help_text='Максимум 400 символов.')
    image = models.ImageField("Изображение", upload_to="", blank=True)

    class Meta:
        verbose_name = "Публикацию"
        verbose_name_plural = "Публикации"


class Comment(models.Model):
    user = models.ForeignKey("account.User", verbose_name='Пользователь', related_name='user_comment',
                             on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, verbose_name='Публикация', related_name='comments',
                                    on_delete=models.CASCADE)
    text = models.TextField("Текст комментария")
    date = models.DateTimeField("Дата публикации", default=timezone.now())

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"
        ordering = ['-date']