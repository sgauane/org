from apps.reg.models import Organizacao, Endereco, Imagem


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
            return endereco
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

