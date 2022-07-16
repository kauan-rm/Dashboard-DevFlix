import jwt
import datetime
import time
# from flask import abort

from app.models import User

# def requisitos(campos, chaves):
#     falta = []

#     for campo in campos:
#         if campo not in chaves:
#             falta.append(campo)        
    
#     if falta:
#         abort(422, f"O(s) campo(s) {falta} é(são) obrigatório(s)")
class Serializer:  

    @staticmethod
    def generate_token(secret_key:str, user_id:int, expiration=86400):
        '''
        Gera um token de confirmação com a id do usuário e uma expiração.
        Recebe como retorno um token de 121 caracteres.
        secret_key: str, chave utilizada nas configurações do app
        user_id: int, id do usuário que será confirmada
        expiration: int, número de segundos para expirar o token
        (str, int, int) -> str
        '''
        token = jwt.encode(
            {
                "confirm": user_id,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                       + datetime.timedelta(seconds=expiration)
            },
            secret_key,
            algorithm="HS256"
        )
        return token

   
    @staticmethod
    def verify_auth_token(secret_key:str, token:str, treshold=3600):
        data = jwt.decode(
                token,
                secret_key,
                leeway=datetime.timedelta(seconds=treshold),
                algorithms=["HS256"]
            )
        return User.query.get(data['confirm'])        

    @classmethod
    def test(cls, sleep=1, treshold=10, expiration=10):
        # Método de teste do funcionamento desta classe. Gera um token, e mostra
        # na tela o tempo decorrido até sua expiração.
        # sleep: int, tempo de espera (em segundos) entre os testes
        # treshold: int, tolerância (em segundos) para a expiração
        # expiration: int, tempo para expiração (em segundos) do token
        # (int, int, int) -> None
        token = cls.generate_confirmation_token("kkk", 1, expiration=expiration)
        print(f"TOKEN: {token}\n")
        t = 0
        while t <= expiration + treshold + 1:
            print(f"t = {t} s: {cls.confirm('kkk', 1, token)}")
            time.sleep(sleep)
            t += sleep    