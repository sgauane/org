from apps.reg.models import Organizacao


class OrgDao:

    def getOrg(self, user):
        try:
            print('Entrou no try')
            ogranizacao = Organizacao.objects.get(admin_user=user)
            print(ogranizacao)
            print('Organizacao ok.')
            return ogranizacao
        except Exception as e:
            print('Ops bug, Entrou no exception', str(e))
        return None