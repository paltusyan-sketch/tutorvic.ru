from django.db import models

# Create your models here.

class Subjects(models.Model):
    discipline = models.CharField(max_length=40)
    cost = models.IntegerField(max_length=40)
    package_size = models.IntegerField(max_length=40, default=10)
    discount_percent = models.IntegerField(max_length=40, verbose_name="Discount", help_text="Скидка %", null=True)
    first_lesson_cost = models.IntegerField(max_length=40, null=True, blank=True, verbose_name="Цена пробного занятия")
    def __str__(self):
        return f"{self.discipline}"



class Settings(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Телефон", default='')
    address_1 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес 1", default='')
    address_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес 2", default='')
    is_free = models.BooleanField(default=False, verbose_name="Бесплатно")
    mb_button_text = models.CharField(max_length=100, verbose_name="Текст кноки на телефоне &nbsp;", default='')
    pk_button_text = models.CharField(max_length=100, verbose_name="Текст кноки на компе &nbsp;", default='')
    cost_first = models.CharField(max_length=10, null=True, blank=True, verbose_name="Цена пробного занятия ₽", default='')


    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"
    
    def __str__(self):
        return "Настройки сайта"