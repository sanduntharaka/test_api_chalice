from chalicelib.supabase_module.auth import supabase_login, supabase_logout, supabase_get_user, supabase_signup, supabase_generate_session
from chalicelib.supabase_module.setup_session import setup_session


class AuthService:
    def sign_up(self, email, password):
        try:
            #      "options": {
            #     "email_redirect_to": "https://example.com/welcome",
            # },
            return supabase_signup(
                {
                    'email': email,
                    'password': password,

                })
        except Exception as e:
            raise Exception(str(e))

    def login(self, email, password):
        try:
            return supabase_login({'email': email, 'password': password})
        except Exception as e:
            raise Exception(str(e))

    def logout(self, auth_token, refresh):
        try:
            setup_session(access_token=auth_token, refresh_token=refresh)

            return supabase_logout(auth_token)
        except Exception as e:
            raise Exception(str(e))

    def get_user(self, auth_token):
        try:
            return supabase_get_user(auth_token)
        except Exception as e:
            raise Exception(str(e))

    def verify_user(self, token, refresh):
        try:
            setup_session(access_token=token, refresh_token=refresh)
            return supabase_generate_session()
        except Exception as e:
            raise Exception(str(e))
