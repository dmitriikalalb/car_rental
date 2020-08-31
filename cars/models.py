from django.db import models


# Create your models here.
class AutoKind(models.Model):
    name = models.CharField('Вид автомобиля', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'


class AutoMark(models.Model):
    name = models.CharField('Марка автомобиля', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class Auto(models.Model):
    image = models.ImageField('Картинка автомобиля')
    mark = models.ForeignKey(AutoMark, on_delete=models.CASCADE)
    model = models.CharField('Модель автомобиля', max_length=200)
    kind = models.ForeignKey(AutoKind, on_delete=models.CASCADE)
    year_of_issue = models.DateField('Дата выпуска')
    vin = models.CharField('VIN', max_length=200)
    description = models.TextField('Описание автомобиля')
    amount = models.IntegerField('Количество доступных автомобилей')

    def __str__(self):
        return str(self.mark)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Zayavka(models.Model):
    fio = models.CharField('ФИО', max_length=255)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    phone = models.CharField('Телефон', max_length=30)
    email = models.CharField('Email', max_length=100)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    status = models.CharField('Статус', max_length=30, choices=[('Рассмотренно', 'Рассмотренно'),
                                                                ('Не рассмотренно', 'Не рассмотренно')])

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class AccountingCars(models.Model):
    zayavka = models.ForeignKey(Zayavka, on_delete=models.CASCADE)
    choice = [('Машина у клиента', 'Машина у клиента'), ('Машина в гараже', 'Машина в гараже')]
    status = models.CharField('Статус', max_length=100, choices=choice)

    def __str__(self):
        return str(self.zayavka)

    class Meta:
        verbose_name = 'Учет'
        verbose_name_plural = 'Учеты'

