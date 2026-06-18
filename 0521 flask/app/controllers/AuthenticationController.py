class AuthenticationController:
    def login(form):
        print('O usuário {} fez login, lembrar = {}'.format(form.username.data, form.remember_me.data))
        return True
    
    def singup(form):
        print('O usuário {} cadastrou-se.'.format(form.username.data))
        return True