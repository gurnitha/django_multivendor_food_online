from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts'

    # Use ready() function to make signals works
    def ready(self):
        import app.accounts.signals
