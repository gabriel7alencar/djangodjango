# djangodjango/craseapp/views.py

from django.shortcuts import render
# Importa todos os modelos e o formulário
from .models import MapeamentoCrase, TermoRegente, TermoRegido
from .forms import ConsultaCraseForm


# --- FUNÇÃO 1: LISTAGEM ESTATICA (/listagem/) ---
def validar_crase(request):
    """
    Busca todos os mapeamentos cadastrados e determina se a crase deve ou não ocorrer.
    """
    # select_related é crucial para performance e segurança ao acessar FKs
    mapeamentos = MapeamentoCrase.objects.all().select_related('regente', 'regido', 'regra')

    lista_resultado = []

    for map in mapeamentos:
        crase_condicao_atendida = map.regente.exige_preposicao and map.regido.aceita_artigo

        regra_aplicada = map.regra.nome_regra if map.regra else "N/A"

        resultado = {
            'regente_termo': map.regente.termo,
            'regido_termo': map.regido.termo,
            'exige_preposicao': map.regente.exige_preposicao,
            'aceita_artigo': map.regido.aceita_artigo,
            'regra_aplicada': regra_aplicada,
            'observacao': map.observacao,
            'crase_ocorre': crase_condicao_atendida,
            'resultado_sintese': f"{map.regente.termo} **{'à' if crase_condicao_atendida else 'a'}** {map.regido.termo}",
        }
        lista_resultado.append(resultado)

    context = {
        'resultados_crase': lista_resultado,
        'titulo': "Validação de Crase: Preposição + Artigo"
    }

    return render(request, 'craseapp/validacao_crase.html', context)


# --- FUNÇÃO 2: CONSULTA DINÂMICA COM FORMULÁRIO (Página Principal: /) ---
def consulta_dinamica(request):
    """Processa o formulário de consulta E carrega todos os mapeamentos para a aba principal."""
    resultado_consulta = None

    # 1. Carrega o QuerySet do DB
    mapeamentos_qs = MapeamentoCrase.objects.all().select_related('regente', 'regido', 'regra')

    # 2. PROCESSA A QUERYSET E ADICIONA O NOVO ATRIBUTO 'crase_ocorre' EM CADA OBJETO
    # Isso é necessário para evitar o TemplateSyntaxError no HTML.
    todos_mapeamentos_list = []
    for map in mapeamentos_qs:
        map.crase_ocorre = map.regente.exige_preposicao and map.regido.aceita_artigo
        todos_mapeamentos_list.append(map)

    if request.method == 'POST':
        form = ConsultaCraseForm(request.POST)

        if form.is_valid():
            regente_selecionado = form.cleaned_data['regente']
            regido_selecionado = form.cleaned_data['regido']

            crase_ocorre = regente_selecionado.exige_preposicao and regido_selecionado.aceita_artigo

            try:
                mapeamento = MapeamentoCrase.objects.get(
                    regente=regente_selecionado,
                    regido=regido_selecionado
                )
                regra_aplicada = mapeamento.regra.nome_regra
            except MapeamentoCrase.DoesNotExist:
                regra_aplicada = "Regra Lógica Padrão (Combinação não mapeada)"

            resultado_consulta = {
                'regente': regente_selecionado.termo,
                'regido': regido_selecionado.termo,
                'preposicao_ok': regente_selecionado.exige_preposicao,
                'artigo_ok': regido_selecionado.aceita_artigo,
                'crase_ocorre': crase_ocorre,
                'regra': regra_aplicada,
                'sintese': f"**{regente_selecionado.termo}** {'à' if crase_ocorre else 'a'} **{regido_selecionado.termo}**",
            }
            form = ConsultaCraseForm()

    else:
        form = ConsultaCraseForm()

    context = {
        'form': form,
        'resultado': resultado_consulta,
        'todos_mapeamentos': todos_mapeamentos_list,  # Passamos a lista processada
    }
    return render(request, 'craseapp/consulta_dinamica.html', context)