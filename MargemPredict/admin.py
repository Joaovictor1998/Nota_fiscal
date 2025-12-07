from django.contrib import admin
from .models import SimulaçãoFiscal 


class SimulaçãoFiscalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'valor_bruto',
        'imposto_percentual',
        'valor_imposto',
        'valor_liquido',
        'data_simulacao'
    )

    search_fields = ('valor_bruto', 'valor_liquido')

admin.site.register(SimulaçãoFiscal, SimulaçãoFiscalAdmin)


