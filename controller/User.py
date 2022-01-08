from model.User import User

class UserController():
    def __init__(self):
        self.user_model = User()
    
    def login(self, email, password):
        self.user_model.email = email # Pega os dados de e-mail e salva no atributo da model de usuário
        
        result = self.user_model.get_user_by_email() # Verifica se o usuário existe no banco de dados
        if result is not None:
            # Verifica se a senha que o usuário enviou, agora convertido em HASH, é igual a senha desse usuário no BD.
            res = self.user_model.verify_password(password, result.password) 
            if res:
                return result
            else:
                return {}
        
        return {}

        def recovery(email):
            return ''
