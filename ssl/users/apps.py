from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'ssl.users'
    verbose_name = "Usuários"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
