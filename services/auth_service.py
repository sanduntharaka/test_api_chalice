from supabase_module.auth import supabase_login, supabase_logout, supabase_get_user, supabase_signup


class AuthService:
    def sign_up(self, email, password):
        try:
            return supabase_signup({'email': email, 'password': password})
        except Exception as e:
            raise Exception(str(e))

    def login(self, email, password):
        try:
            return supabase_login({'email': email, 'password': password})
        except Exception as e:
            raise Exception(str(e))

    def logout(self, auth_token):
        try:
            return supabase_logout(auth_token)
        except Exception as e:
            raise Exception(str(e))

    def get_user(self, auth_token):
        try:
            return supabase_get_user(auth_token)
        except Exception as e:
            raise Exception(str(e))
