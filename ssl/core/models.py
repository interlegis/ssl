from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from model_utils import Choices
from ssl.users.models import User
from ssl.orgao.models import Orgao
import django.utils.timezone


class Obra(models.Model):
    titulo = models.CharField(max_length=250,
                              blank=False,
                              verbose_name=_('Título'))
    qtd_disponivel = models.PositiveIntegerField(blank=False,
                                                 verbose_name=_('Quantidade Disponível'))


    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class CampanhaDoacao(models.Model):
    data_inicio = models.DateField(verbose_name=_('Data Início'),
                                   blank=False)
    data_fim = models.DateField(verbose_name=_('Data Fim'),
                                blank=False)

    class Meta:
        verbose_name = 'Campanha de Doação'
        verbose_name_plural = 'Campanhas de Doação'
        ordering = ['-data_inicio']

    def __str__(self):
        if self.data_inicio and self.data_fim:
            return 'Campanha de %s - %s' % (self.data_inicio.strftime("%d/%m/%Y"),
                                self.data_fim.strftime("%d/%m/%Y"))
        else:
            return 'Campanha de Doação'

    def get_absolute_url(self):
        return reverse('campanha:detail', kwargs={'pk': self.pk})


#class StatusPedido(models.Model):
#    sigla = models.CharField(max_length=1, unique=True, verbose_name='Sigla')
#    descricao = models.TextField(unique=True, verbose_name='Status do Pedido')


class Pedido(models.Model):

    STATUS_CHOICES = Choices(
        ('DT', 'Deferido totalmente', 'Deferido Totalmente'),
        ('I', 'Indeferido', 'Indeferido'),
        ('DP', 'Deferido parcialmente', 'Deferido Parcialmente'),
    )
    campanha = models.ForeignKey(CampanhaDoacao,
                                 on_delete=models.PROTECT,
                                 verbose_name=_('Campanha de Doação'))

    data_pedido = models.DateField(verbose_name=_('Data do Pedido'),
                                   default=django.utils.timezone.now,
                                   blank=False)

    #    status_pedido = models.ForeignKey(StatusPedido, verbose_name='Status do Pedido')
    status_pedido = models.CharField(max_length=1,
                                     verbose_name=_('Esfera Federação'),
                                     choices=STATUS_CHOICES)



class ItemPedido(models.Model):
    obra = models.ForeignKey(Obra, verbose_name=_('Obra'),
                             on_delete=models.CASCADE)
    data_requisicao = models.DateField(verbose_name=_('Data Requisição'))
    quantidade = models.PositiveIntegerField(verbose_name=_('Quantidade'))
    # status = models.ForeignKey(StatusRequisicao,
    #                            on_delete=models.PROTECT,
    #                            verbose_name='Status da Requisição')

    pedido = models.ForeignKey(Pedido, verbose_name=_('Item do pedido'),
                               on_delete=models.CASCADE)


class Representacao(models.Model):
    representante = models.OneToOneField(User,
                                         verbose_name=_('Representante'),
                                         on_delete=models.PROTECT,
                                         null=True)

    orgao_representado = models.ForeignKey(Orgao,
                                           verbose_name=_('Órgão Representado'),
                                           on_delete=models.PROTECT)

    data_inicio_representacao = models.DateField(verbose_name=_('Data Início da Representação'),
                                                 blank=False)
    data_fim_representacao = models.DateField(verbose_name=_('Data Fim da Representação'))

    class Meta:
        verbose_name = _('Representação')
        verbose_name_plural = _('Representações')
        ordering = ['orgao_representado', 'representante']

    def __str__(self):
        return str('Representação de(a) {}'.format(self.orgao_representado))


class ArquivoExcel(models.Model):
    arquivo = models.FileField()
    data_upload = models.DateTimeField(auto_now_add=True)
