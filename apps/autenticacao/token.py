from datetime import datetime
from random import random

from apps.autenticacao.models import Token


def genToken():
    rand = random.randrange(100000, 999999)
    token = str(rand)
    return token

def saveToken(user):
    tk = Token()

    print('compose token')
    tomorrowtimestamp = datetime.today()
    tk.ususario = user
    tk.token = genToken()
    tk.deta_validade = tomorrowtimestamp
    tk.save()
    print('token saved')
    return tk.token