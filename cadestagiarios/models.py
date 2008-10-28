# -*- coding: utf-8 -*-

from django.db import models
from datetime import date

# Create your models here.
class Banco(models.Model):
    numero_do_banco = models.CharField('Número do Banco', max_length = 3, unique = True)
    nome_do_banco = models.CharField('Nome do Banco', max_length = 50, unique = True)

    def __unicode__(self):
        return self.nome_do_banco

    class Admin:
        list_display = ('numero_do_banco', 'nome_do_banco')

class Projeto(models.Model):
    numero_do_projeto = models.IntegerField('Número do Projeto na Funpar')
    nome_do_projeto = models.CharField('Nome do Projeto', max_length = 50, unique = True)
    banco = models.ForeignKey(Banco)
    cc_agencia = models.CharField('Agencia', max_length = 10)
    cc_num_conta = models.CharField('Conta Corrente', max_length = 20)

    def __unicode__(self):
        return self.nome_do_projeto

    class Admin:
        list_display = ('numero_do_projeto', 'nome_do_projeto')

class Cidade(models.Model):
    cidade = models.CharField('Cidade', max_length=35)

    def __unicode__(self):
        return self.cidade
    
    class Meta:
        ordering = ('cidade',)
    class Admin:
        pass

class Estado(models.Model):
    sigla = models.USStateField()
    nome = models.CharField(max_length = 35)
    
    def __unicode__(self):
        return self.nome
    
    #class Meta:
    #    ordering = ('nome',)
    
    class Admin:
        pass

class ConjAtividade(models.Model):
    descricaoounome = models.CharField('Descrição', max_length=25)
    
    def __unicode__(self):
        return self.descricaoounome
    
    class Admin:
        pass

class Atividade(models.Model):
    conjatividade = models.ForeignKey(ConjAtividade, edit_inline=models.STACKED, num_in_admin=1)
    atividade = models.TextField(core=True)

class ConjAtividadeEspecifica(models.Model):
    descricaoounome = models.CharField('Descrição', max_length=25)

    def __unicode__(self):
        return self.descricaoounome

    class Admin:
        pass

#Atividade especifica do curso do estudante
class AtividadeEspecifica(models.Model):
    conjatividade = models.ForeignKey(ConjAtividadeEspecifica, edit_inline=models.TABULAR, num_in_admin=1)
    atividade = models.TextField(core=True)

class ConjConjAtividades(models.Model):
    descricaoounome = models.CharField('Descrição', max_length=25)
    atividadesdoprojeto = models.ForeignKey(ConjAtividade)
    atividadesdafuncao = models.ForeignKey(ConjAtividadeEspecifica)
    #atividadesdocurso = models.ForeignKey(ConjAtividade)

class Coordenador(models.Model):
    nome = models.CharField(max_length=45)
    cargo = models.CharField(max_length=35)
    telefone = models.CharField(max_length=20)
    ramal = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.nome
    
    #class Meta:
    #    ordering = ('nome',)
        
    class Admin:
        list_display = ('nome','telefone')

class SubProjeto(models.Model):
    BALNRES = (('Balneabilidade','Balneabilidade'),('Resíduos','Resíduos'),('QG','Administração'),('ARRUMAR','ARRUMAR'))
    balnres = models.CharField('Balneabilidade / Residuos', max_length = 23, choices=BALNRES)
    coordenador = models.ForeignKey(Coordenador)
    cidade = models.ForeignKey(Cidade, blank=True, null=True)
    
    def __unicode__(self):
        return "%s - %s - %s" % (self.coordenador, self.balnres, self.cidade)
    
    #class Meta:
    #    ordering = ('coordenador',)
        
    class Admin:
        pass

class InstituicaoDeEnsino(models.Model):
    nome = models.CharField(max_length = 75)
    
    def __unicode__(self):
        return self.nome
    
    #class Meta:
    #    ordering = ('nome',)
        
    class Admin:
        pass
        
class Curso(models.Model):
    nome_do_curso = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.nome_do_curso
        
    class Admin:
        pass
    

class Estagiario(models.Model):
    projeto = models.ForeignKey(Projeto)
    nome_do_estagiario = models.CharField("Nome", max_length=70)
    nome_do_solicitante = models.CharField("Nome do Solicitante", max_length=50, blank=True)
    subprojeto = models.ForeignKey(SubProjeto, null=True, blank=True)
    end_rua = models.CharField('Logradouro', max_length = 45, blank=True)
    end_num = models.CharField('Núm.', max_length = 15, blank=True)
    end_compl = models.CharField('Coml', max_length = 30, blank=True)
    telefones = models.CharField('Fones', max_length = 45, blank=True)
    end_bairro = models.CharField('Bairro', max_length = 40, blank=True)
    end_cidade = models.ForeignKey(Cidade, null=True, blank=True)
    end_estado = models.ForeignKey(Estado, null=True, blank=True)
    conj_atividades = models.ForeignKey(ConjAtividade, null=True, blank=True)
    #bloco1 = models.BooleanField('14/12/2007 a 14/01/2008')
    #bloco2 = models.BooleanField('15/01/2008 a 17/02/2008')
    bloco1 = models.BooleanField()
    bloco2 = models.BooleanField()
    #coordenador = models.ForeignKey(Coordenador)
    #retirei pois ja esta no subprojeto 
    instituicao_de_ensino = models.ForeignKey(InstituicaoDeEnsino, null=True, blank=True)
    bloco1_valor = models.DecimalField('Bloco 1 R$:', max_digits=7, decimal_places=2, null=True, blank=True)
    bloco2_valor = models.DecimalField('Bloco 2 R$:', max_digits=7, decimal_places=2, null=True, blank=True)
    data_de_inicio_do_estagio = models.DateField('Início', null=True, blank=True)
    data_de_termino_do_estagio = models.DateField('Término', null=True, blank=True)
    data_prevista_para_inicio = models.DateField('Data Prevista para Início', null=True, blank=True)
    data_prevista_para_termino = models.DateField('Data Prevista para Término', null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    num_matricula_ufpr = models.CharField(max_length=25, null=True, blank=True, aka='num_matricula')
    
    data_da_ultima_atualizacao = models.DateField(auto_now=True, null=True)
    data_do_cadastro = models.DateField(auto_now_add=True, null=True)
    
    numero_no_ciee = models.PositiveIntegerField(null=True,blank=True)

    nome_da_mae = models.CharField(max_length=65, null=True, blank=True)
    data_nasc_mae = models.DateField(null=True, blank=True)

    estudante_da_ufpr = models.BooleanField('Estuda na UFPR?', null=True, blank=True)
    
    #local_do_contrato = models.ForeignKey('Local')
    #local_do_xerox_da_identidade = models.ManyToManyField('Local')
    #local_do_xerox_do_cpf = models.ManyToManyField('Local')
    #local_do_comprovante_de_matricula = models.ManyToManyField('Local')
    #local_do_comprovante_de_conta_corrente = models.ManyToManyField('Local')
    #local_do_comprovante_de_residencia = models.ManyToManyField('Local')
    
    # apagados - mas nao da pra retirar daqui senao da erro no deseb
    teste2 = models.TextField(null=True, blank=True)
    teste3 = models.IntegerField(null=True, blank=True)
    teste4 = models.CharField(max_length=2, null=True, blank=True)
    teste = models.CharField(max_length = 7, null=True, blank=True)
    rg = models.CharField(max_length = 25, blank=True, null=True)
    cpf = models.CharField(max_length = 25, blank=True, null=True)
    conta_corrente = models.CharField(max_length = 25, blank=True, null=True)
    agencia = models.CharField(max_length = 10, blank=True, null=True)
    banco = models.ForeignKey(Banco, null=True, blank=True)
    falta_pagamento = models.BooleanField('Não Recebeu', null=True, blank=True)
    reclamou_pagamento = models.BooleanField('Reclamou Pag.', null=True, blank=True)
    obs = models.TextField(null=True, blank=True)
    verificar_pagamento = models.BooleanField('Verif. Pag.', null=True, blank=True)
    curso = models.ForeignKey(Curso, null=True, blank=True)
    pagamento_pendente = models.DecimalField(max_digits=7, decimal_places = 2, null=True, blank=True)
    
    def cidade_do_subprojeto(self):
        return self.subprojeto.cidade
    
    def media_dos_valores_dos_blocos(self):
        valor1 = self.bloco1_valor or 0
        valor2 = self.bloco2_valor or 0
        return (valor1 + valor2) / 2
    media_dos_valores_dos_blocos.short_description = "Média R$"
    
    def esta_trabalhando(self):
        #return self.data_de_inicio_do_estagio < date.today() < self.data_de_termino_do_estagio
        if self.data_de_termino_do_estagio and self.data_de_termino_do_estagio:
            return self.data_de_inicio_do_estagio < date.today() < self.data_de_termino_do_estagio
        else:
            return None  
            
    esta_trabalhando.short_description = "Na Área?"
    esta_trabalhando.boolean = True
    
    def __unicode__(self):
        return self.nome_do_estagiario
    
    #class Meta:
        #ordering = ('nome_do_estagiario',)

    def pag_ok(self):
        return not self.falta_pagamento
    pag_ok.boolean = True
        
    def nao_reclamou(self):
        return not self.reclamou_pagamento
    nao_reclamou.boolean = True
    
    def verificado(self):
        if self.verificar_pagamento:
            return not self.verificar_pagamento
        else:    
            return None
    verificado.boolean=True
    
    class Admin:
        fields = (
            (None, {'fields':(
                    'nome_do_estagiario','falta_pagamento','reclamou_pagamento',
                    'verificar_pagamento', 'email', 'subprojeto','numero_no_ciee',
                    'rg','cpf','num_matricula_ufpr','obs','pagamento_pendente')}),
            ('Telefones', {'fields':
                    ('telefones',)}),
            ('Filiação', {'fields':('nome_da_mae','data_nasc_mae')}),
            ('Outros', {'fields':('projeto','nome_do_solicitante')}),
            ('Banco',{'fields':('banco','agencia', 'conta_corrente')}),
            ('Endereço', {'fields':('end_rua', 'end_num', 'end_compl', 'end_bairro',
                                    'end_cidade','end_estado')}),
            #('Atividades', {'fields':('conj_atividades',)}),
            ('Períodos / Blocos', {'fields':('bloco1', 'bloco2')}),
            ('Instituição de Ensino', 
                {'fields':('instituicao_de_ensino','estudante_da_ufpr','curso')}),
            ('Valor da Bolsa', {'fields':('bloco1_valor','bloco2_valor'),'classes':'collapse'}),
            ('Período do Estágio', 
                {'fields':('data_prevista_para_inicio','data_prevista_para_termino','data_de_inicio_do_estagio','data_de_termino_do_estagio')}),
            #('Testes', {'fields':('teste2',)}),
            )
        list_display = (
            #'nome_do_estagiario', 'telefones', 'cpf','rg','pag_ok','recpag_ok','verificado',
            'nome_do_estagiario', 'telefones','pag_ok', #,'nao_reclamou','verificado',
            #'nome_do_estagiario', 'telefones', 'cpf','rg','falta_pagamento','reclamou_pagamento','verificar_pagamento',
            'data_de_inicio_do_estagio','data_de_termino_do_estagio')
        #list_display = ('nome_do_estagiario','telefones')
        #list_filter = ('estudante_da_ufpr',)
        list_per_page = 25
        search_fields = ['nome_do_estagiario']
        list_filter = ('falta_pagamento','reclamou_pagamento', 'verificar_pagamento', 'subprojeto','instituicao_de_ensino','end_cidade')#,'data_da_ultima_atualizacao','data_do_cadastro')
        ordering = ('nome_do_estagiario',)
        save_on_top = True
        #date_hierarchy = 'data_da_ultima_atualizacao'
        

#class SuperEstagiario(Estagiario):
#    super_nome = models.CharField(max_length = 10, blank=True)
#    teste2 = models.IntegerField(blank=True)
#    
#    class Admin:
#        pass
        
class Local(models.Model):
    """ Local onde pode estar o contrato 
    """
    nome_do_local = models.CharField(max_length = 75)
    
    def __unicode__(self):
        return self.nome_do_local
        
    #class Meta:
    #    ordering = ('nome_do_local',)
    
    class Admin:
        pass

#class Contrato(models.Model):
#    local_atual = models.ForeignKey(Local)
#    obs = models.TextField()

class EstadoDoDocumento(models.Model):
    estado = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.estado
    
    class Admin:
        list_filter = ('estado',)
    
class TipoDeDocumento(models.Model):
    tipo = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.tipo
    
    class Admin:
        pass

class Documento(models.Model):
    estagiario = models.ForeignKey(Estagiario)
    #tipo = models.CharField('desconsiderar este campo',max_length = 50, blank=True)
    tipo_de_documento = models.ForeignKey(TipoDeDocumento, core=True, blank=True, null=True)
    local_atual = models.ForeignKey(Local, blank=True, null=True)
    data_de_envio_ou_chegada = models.DateTimeField(blank=True, null=True)
    preenchido = models.BooleanField(blank=True, null=True)
    assinado = models.BooleanField(blank=True, null=True)
    estado = models.ForeignKey(EstadoDoDocumento, null=True, blank=True)
    obs = models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s  - Doc.: %s  - Local: %s" % (self.estagiario, self.tipo_de_documento, self.local_atual)
        #return self.estagiario
    
    class Meta:
        ordering = ('estagiario',)
        
    class Admin:
        list_display = ('estagiario','tipo_de_documento','local_atual','preenchido','assinado')
        list_filter = ('tipo_de_documento','local_atual','data_de_envio_ou_chegada','preenchido','assinado','estagiario')
        search_fields = ['estagiario']       # não funcionou com foreign

#class ConjDeDocumentos(models.Model):
    #documento = models.ForeignKey(Documento)
    #estagiario = models.OneToOneField(Estagiario)

class TipoDePendencia(models.Model):
    tipo = models.CharField(max_length=35)
    
    def __unicode__(self):
        return self.tipo
        
    #class Meta:
    #    ordering = ('tipo',)
        
    class Admin:
        pass
        
class Pendencia(models.Model):
    estagiario = models.ForeignKey(Estagiario, edit_inline=models.TABULAR, num_in_admin=1, num_extra_on_change=1)
    tipo_de_pendencia = models.ForeignKey(TipoDePendencia, core=True)
    data_da_atualizacao = models.DateField(auto_now=True, null=True)
    
    #class Meta:
    #    ordering = ('estagiario',)
        
    def __unicode__(self):
        return u"%s  -  %s" % (self.estagiario, self.tipo_de_pendencia)
    
    class Admin:
        list_filter = ('tipo_de_pendencia','data_da_atualizacao','estagiario')
        #search_fields = ('estagiario',)
        date_hierarchy = 'data_da_atualizacao'

class TipoDeContatamento(models.Model):
    descricao_do_tipo = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.descricao_do_tipo
    
    class Admin:
        pass
        
class Contatamento(models.Model):
    estagiario = models.ForeignKey(Estagiario, edit_inline=models.TABULAR, num_in_admin=1, num_extra_on_change=1)
    data_e_hora = models.DateTimeField()
    tipo_de_contatamento = models.ForeignKey(TipoDeContatamento, core=True, blank=True, null=True)
    ocorrido = models.CharField(max_length = 100, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.estagiario
        
    def pag_ok(self):
        return self.estagiario.pag_ok()
    pag_ok.boolean = True
    
    class Admin:
        list_display = ('estagiario','data_e_hora','tipo_de_contatamento','ocorrido','pag_ok')
        date_hierarchy = 'data_e_hora'
        
        
class Instituicao(models.Model):
    nome = models.CharField(max_length = 85)
    
    def __unicode__(self):
        return self.nome
    
    class Admin:
        pass
        
class Contato(models.Model):
    nome = models.CharField(max_length = 75)
    telefone = models.CharField(max_length = 45)
    instituicao = models.ForeignKey(Instituicao, null=True, blank=True)

    def __unicode__(self):
        return self.nome
    
    class Admin:
        list_display = ('nome', 'instituicao','telefone')
        search_fields = ('nome','instituicao')
 
        
class ItemFotografado(models.Model):
    " Pode conter várias fotos "
    nome = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.nome
        
    class Admin:
        pass

class Foto(models.Model):
    desc = models.CharField(max_length = 200, blank=True, core=True)
    foto = models.ImageField(upload_to="fotos", core=True)
    item_fotografado = models.ForeignKey(ItemFotografado, edit_inline=models.TABULAR)
    