from django.db import models
from django.contrib.auth.models import User  # Importe a classe User do Django


class Transacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=1, choices=[
                            ('E', 'Entrada'), ('S', 'Saída')])

    def __str__(self):
        return self.descricao
