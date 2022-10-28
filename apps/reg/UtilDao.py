from apps.home.models import Perguntas, SobreNos, Valores
from apps.reg.models import Organizacao, Endereco, Imagem, Pessoa, Membro, ModificadoresContrato


class UtilDao:

    def getOrgByUser(self, user):
        try:
            print('Entrou no try')
            ogranizacao = Organizacao.objects.get(admin_user=user)
            print(ogranizacao)
            print('Organizacao ok.')
            return ogranizacao
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None

    def getOrg(self, id):
        try:
            print('Entrou no try')
            ogranizacao = Organizacao.objects.get(pk=id)
            print(ogranizacao)
            print('Organizacao ok.')
            return ogranizacao
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None

    def getAddressByOrg(self, org):
        try:
            print('Entrou no try')
            endereco = Endereco.objects.filter(entidade=org.id, data_fim=None)
            print(endereco)
            print('Address ok.')
            return endereco[0]
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None

    def getAddress(self, id):
        try:
            print('Entrou no try')
            endereco = Endereco.objects.get(pk=id)
            print(endereco)
            print('Address ok.')
            return endereco
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def getImagem(self, id):
        try:
            print('Entrou no try')
            img = Imagem.objects.get(pk=id)
            print(img)
            print('Address ok.')
            return img
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def getPessoa(self, id):
        try:
            print('Entrou no try')
            obj = Pessoa.objects.get(pk=id)
            print(obj)
            print('Object ok. -> ')
            return obj
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def findAllMembrosByOrg(self, orgId):
        try:
            print('Entrou no try')
            lista = Membro.objects.filter(contratante=orgId)
            print(lista)
            print('Object ok. -> ')
            return lista
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def getModificadorContrato(self, id):
        try:
            print('Entrou no try')
            obj = ModificadoresContrato.objects.get(pk=id)
            print(obj)
            print('Object ok. -> ')
            return obj
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def getMembro(self, id):
        try:
            print('Entrou no try')
            obj = Membro.objects.get(pk=id)
            print(obj)
            print('Object ok. -> ')
            return obj
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def findAllPerguntas(self):
        try:
            print('Entrou no try')
            lista = Perguntas.objects.all()
            print(lista)
            print('Object ok. -> ')
            return lista
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None

    def findAllPerguntasFrequentes(self):
        try:
            print('Entrou no try')
            lista = Perguntas.objects.filter(activo=True, favorito=True)
            print(lista)
            print('Object ok. -> ')
            return lista
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None


    def getSobreNosByOrg(self, orgId):
        try:
            print('Entrou no try')
            obj = SobreNos.objects.get(organizacao=orgId)
            print(obj)
            print('Object ok. -> ')
            return obj
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None

    def getValores(self, id):
        try:
            print('Entrou no try')
            obj = Valores.objects.get(pk=id)
            print(obj)
            print('Object ok. -> ')
            return obj
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None

    def findAllValoresByOrg(self, orgId):
        try:
            print('Entrou no try')
            lista = Valores.objects.filter(organizacao=orgId)
            print(lista)
            print('Object ok. -> ')
            return lista
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None



