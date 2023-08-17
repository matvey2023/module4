from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils import timezone

User = get_user_model()

class Advertisement(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField("изображение", upload_to="advertisements/")

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y in %H:%M:%S")

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.created_at.strftime("%d.%m.%Y in %H:%M:%S")

    @admin.display(description="картинка")
    def small_image(self):
        if self.image:
            return format_html('<img src="{}" style="width: 55px;">', self.image.url)
        else:
            return 'No image'
