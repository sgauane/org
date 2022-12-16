from django.db import models

from apps.reg.models import ModeloBase, ItemPreco


# Create your models here.
class TipoDebito(ModeloBase):
    designacao = models.CharField(max_length=255)


class Debito(ModeloBase):
    referencia = models.CharField(max_length=11,)
    valor = models.ForeignKey(ItemPreco, on_delete=models.SET_NULL, null=True)
    data_limite = models.DateField()
    tipo = models.ForeignKey(TipoDebito, on_delete=models.SET_NULL, null=True)


class Desconto(ModeloBase):
    valor = models.DecimalField(max_digits=7, decimal_places=2)


class Pagamento(ModeloBase):
    referencia = Debito.referencia
    debito = models.ForeignKey(Debito, on_delete=models.SET_NULL, null=True)
    desconto = models.ForeignKey(Desconto, on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)