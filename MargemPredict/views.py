from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SimulaçãoFiscal # <-- Importe o modelo!

# ... (Sua função prever_margem aqui) ...

@csrf_exempt
def simular_nf(request):
    
    # Inicializa o contexto com valores nulos para a primeira carga da página
    context = {'valor_liquido': None, 'erro': None} 
    
    if request.method == 'POST':
        try:
            # 1. CAPTURA E CONVERSÃO DOS DADOS
            valor_bruto = float(request.POST.get('valor_bruto').replace(',', '.'))
            imposto_percentual = float(request.POST.get('imposto_percentual').replace(',', '.'))

            # 2. CÁLCULO DA NOTA FISCAL
            taxa_imposto = imposto_percentual / 100 
            valor_imposto = valor_bruto * taxa_imposto
            valor_liquido_calc = valor_bruto - valor_imposto
            
            valor_liquido_final = round(valor_liquido_calc, 2)
            valor_imposto_final = round(valor_imposto, 2)
            
            # 3. SALVAR A SIMULAÇÃO NO BANCO DE DADOS
            SimulaçãoFiscal.objects.create(
                valor_bruto=valor_bruto,
                imposto_percentual=imposto_percentual,
                valor_imposto=valor_imposto_final,
                valor_liquido=valor_liquido_final
            )
            
            # 4. PREPARAR O CONTEXTO DE SUCESSO
            context = {
                'valor_bruto': round(valor_bruto, 2),
                'imposto_percentual': round(imposto_percentual, 2),
                'valor_liquido': valor_liquido_final,
                'valor_imposto': valor_imposto_final,
                'erro': None,
            }
            
        except AttributeError:
             # Este erro pode ocorrer se o input estiver vazio
             context['erro'] = "Erro: Por favor, preencha todos os campos."
        except ValueError:
            # Captura se o usuário digitar texto ou ponto/vírgula inválidos
            context['erro'] = "Erro: Por favor, insira apenas valores numéricos válidos."
        except Exception as e:
            # Captura qualquer outro erro (incluindo erro de banco de dados/SQL)
            context['erro'] = f"Erro desconhecido: Falha no salvamento dos dados. Verifique a migração. {e}"

    # Retorna o template com o contexto (sucesso ou erro)
    return render(request, 'margem_predict/nf_simulador.html', context)
