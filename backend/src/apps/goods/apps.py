from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.goods'
    verbose_name = "Товары и категории"

    def ready(self):
        import apps.goods.signals
