from django.db import models

class SimulaçãoFiscal(models.Model):
    # Valores de Entrada
    valor_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    imposto_percentual = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Valores Calculados (O Resultado)
    valor_imposto = models.DecimalField(max_digits=10, decimal_places=2)
    valor_liquido = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Rastreamento
    data_simulacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"NF {self.id} | Bruto R$ {self.valor_bruto} | Líquido R$ {self.valor_liquido} ({self.data_simulacao.strftime('%d/%m %H:%M')})"
