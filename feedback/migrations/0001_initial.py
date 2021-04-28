# Generated by Django 3.1.7 on 2021-04-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=130, verbose_name='ФИО')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('gender', models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский')], default=1, verbose_name='Пол')),
                ('service', models.IntegerField(choices=[(1, 'Покупка квартиры'), (2, 'Работа персонала'), (3, 'Использование сайта'), (4, 'Прочее')], default=1, verbose_name='О какой услуге Вы хотите оставить отзыв?')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('notice', models.BooleanField(default=False, verbose_name='Получать новости о новых предложениях на электронную почту?')),
                ('email', models.EmailField(max_length=130, verbose_name='E-Mail')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
