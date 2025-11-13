# djangodjango/craseapp/models.py

from django.db import models


# Modelo 1: RegraCrase
class RegraCrase(models.Model):
    nome_regra = models.CharField(max_length=100)
    descricao = models.TextField()
    crase_obrigatoria = models.BooleanField()

    class Meta:
        verbose_name_plural = "Regras de Crase"

    def __str__(self):
        # SIMPLIFICADO: Retorna apenas o nome do campo.
        return self.nome_regra


# Modelo 2: TermoRegente
class TermoRegente(models.Model):
    TIPOS_REGENTE = [
        ('Verbo', 'Verbo'),
        ('Nome', 'Nome'),
        ('LocucaoPrepositiva', 'Locução Prepositiva'),
    ]

    termo = models.CharField(max_length=100, unique=True)
    tipo_regente = models.CharField(max_length=50, choices=TIPOS_REGENTE)
    exige_preposicao = models.BooleanField(default=True)

    def __str__(self):
        # SIMPLIFICADO: Retorna apenas o termo para evitar chamadas complexas
        return self.termo


# Modelo 3: TermoRegido
class TermoRegido(models.Model):
    CLASSES_GRAMATICAIS = [
        ('Substantivo', 'Substantivo'),
        ('Pronome', 'Pronome'),
        ('LocucaoAdverbial', 'Locução Adverbial'),
    ]
    GENEROS = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
    ]

    termo = models.CharField(max_length=100, unique=True)
    classe_gramatical = models.CharField(max_length=50, choices=CLASSES_GRAMATICAIS)
    genero = models.CharField(max_length=10, choices=GENEROS)
    aceita_artigo = models.BooleanField()

    def __str__(self):
        # SIMPLIFICADO: Retorna apenas o termo para evitar chamadas complexas
        return self.termo


# Modelo 4: MapeamentoCrase (Tabela de Relacionamento)
class MapeamentoCrase(models.Model):
    regente = models.ForeignKey('TermoRegente', on_delete=models.CASCADE)
    regido = models.ForeignKey('TermoRegido', on_delete=models.CASCADE)
    regra = models.ForeignKey('RegraCrase', on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Mapeamento de Crase"
        verbose_name_plural = "Mapeamentos de Crase"
        unique_together = ('regente', 'regido')

    def __str__(self):
        # SIMPLIFICADO: Retorna a string mais segura, usando apenas os termos
        return f"{self.regente.termo} + {self.regido.termo}"