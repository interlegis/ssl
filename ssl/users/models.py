from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    name = models.CharField(_('Nome do Usuário'), blank=True, max_length=255)
    phone = models.BigIntegerField(_('Telefone'), blank=True,
                                   null=True,
                                help_text="Preencha com DDD e o número (sem símbolos especiais")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
