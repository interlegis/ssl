from django.db import models
from model_utils import Choices

class Obra(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='Título')

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class CampanhaDoacao(models.Model):
    data_inicio = models.DateField(verbose_name='Data Início')
    data_fim = models.DateField(verbose_name='Data Início')

    class Meta:
        verbose_name = 'Campanha de Doação'
        verbose_name_plural = 'Campanhas de Doação'
        ordering = ['-data_inicio']

    def __str__(self):
        return "Campanha de %s a %s" % (str(self.data_inicio), str(self.data_fim))


#class StatusPedido(models.Model):
#    sigla = models.CharField(max_length=1, unique=True, verbose_name='Sigla')
#    descricao = models.TextField(unique=True, verbose_name='Status do Pedido')


class Pedido(models.Model):

    STATUS_CHOICES = Choices(
        ('DT', 'Deferido totalmente', 'Deferido totalmente'),
        ('I', 'Indeferido', 'Indeferido'),
        ('DP', 'Deferido parcialmente', 'Deferido parcialmente'),
    )
    campanha = models.ForeignKey(CampanhaDoacao,
                                 on_delete=models.PROTECT,
                                 verbose_name='Campanha de Doação')

    data_pedido = models.DateField(verbose_name='Data Início')

    #    status_pedido = models.ForeignKey(StatusPedido, verbose_name='Status do Pedido')
    status_pedido = models.CharField(max_length=1,
                                     verbose_name='Esfera Federação',
                                     choices=STATUS_CHOICES)



class ItemPedido(models.Model):
    obra = models.ForeignKey(Obra, verbose_name='Obra', on_delete=models.CASCADE)
    data_requisicao = models.DateField(verbose_name='Data Requisição')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    # status = models.ForeignKey(StatusRequisicao,
    #                            on_delete=models.PROTECT,
    #                            verbose_name='Status da Requisição')

    pedido = models.ForeignKey(Pedido, verbose_name='Item do pedido', on_delete=models.CASCADE)

