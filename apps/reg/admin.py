from django.contrib import admin


from apps.reg.models import *

# Register your models
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Pessoa)
admin.site.register(TipoDocumento)
admin.site.register(TipoOrganizacao)
admin.site.register(Imagem)
admin.site.register(Organizacao)
admin.site.register(Endereco)
admin.site.register(TipoContrato)
admin.site.register(ModificadoresContrato)
admin.site.register(Contrato)
admin.site.register(Membro)
