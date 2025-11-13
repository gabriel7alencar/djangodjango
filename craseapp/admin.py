from django.contrib import admin
from .models import RegraCrase, TermoRegente, TermoRegido, MapeamentoCrase


# 1. Registro da RegraCrase
@admin.register(RegraCrase)
class RegraCraseAdmin(admin.ModelAdmin):
    list_display = ('nome_regra', 'crase_obrigatoria')
    search_fields = ('nome_regra', 'descricao')


# 2. Registro do TermoRegente
@admin.register(TermoRegente)
class TermoRegenteAdmin(admin.ModelAdmin):
    list_display = ('termo', 'tipo_regente', 'exige_preposicao')
    list_filter = ('tipo_regente', 'exige_preposicao')
    search_fields = ('termo',)


# 3. Registro do TermoRegido
@admin.register(TermoRegido)
class TermoRegidoAdmin(admin.ModelAdmin):
    list_display = ('termo', 'genero', 'aceita_artigo', 'classe_gramatical')
    list_filter = ('genero', 'aceita_artigo', 'classe_gramatical')
    search_fields = ('termo',)


# 4. Registro do MapeamentoCrase (Corrigido para evitar recursão no list_display)
@admin.register(MapeamentoCrase)
class MapeamentoCraseAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista (Usamos IDs para segurança máxima contra recursão)
    list_display = ('id', 'regente_id', 'regido_id', 'regra_id', 'resultado_crase')
    # Filtros laterais
    list_filter = ('regra__crase_obrigatoria',)
    # Campos de pesquisa
    search_fields = ('regente__termo', 'regido__termo', 'regra__nome_regra')

    def resultado_crase(self, obj):
        """Método customizado para exibir o resultado da crase (lógica principal)."""
        # Verifica se o regente exige 'a' E se o regido aceita 'a'
        if obj.regente.exige_preposicao and obj.regido.aceita_artigo:
            return f"Sim: Regra '{obj.regra.nome_regra}'"
        else:
            return "Não: Crase Proibida/Ausente"

    # Define um cabeçalho para a coluna customizada
    resultado_crase.short_description = 'Crase Resultante'