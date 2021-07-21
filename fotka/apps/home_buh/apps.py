from django.apps import AppConfig


class HomeBuhConfig(AppConfig):
    name = 'home_buh'
    verbose_name = 'ХХ. Домашняя Бухгалтерия'

    def ready(self):
        import home_buh.signal
