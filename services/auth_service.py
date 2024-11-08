from supabase_module.auth import supabase_login, supabase_logout, supabase_get_user


class AuthService:
    def login(self, email, password):
        return supabase_login({'email': email, 'password': password})

    def logout(self, auth_token):
        return supabase_logout(auth_token)

    def get_user(self, auth_token):
        return supabase_get_user(auth_token)
