

# app1/context_processors.py


def site_settings(request):
    from .models import Settings
    """
    Добавляет объект настроек сайта в контекст каждого запроса.
    """
    try:
        settings = Settings.objects.get()
    except Settings.DoesNotExist:
        settings = None
    except Settings.MultipleObjectsReturned:
        # Если вдруг их несколько, берем первый (наш save() метод это предотвращает)
        settings = Settings.objects.first()

    return {'site_settings': settings}