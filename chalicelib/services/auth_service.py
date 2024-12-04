from chalicelib.supabase_module.auth import (
    supabase_login,
    supabase_logout,
    supabase_get_user,
    supabase_signup,
    supabase_generate_session,
)
from chalicelib.models.auth_models import AuthTokens


class AuthService:
    def sign_up(self, email: str, password: str) -> dict:
        try:
            return supabase_signup({'email': email, 'password': password})
        except Exception as e:
            raise Exception(str(e))

    def login(self, email: str, password: str) -> dict:
        try:
            return supabase_login({'email': email, 'password': password})
        except Exception as e:
            raise Exception(str(e))

    def logout(self, tokens: AuthTokens) -> dict:
        try:
            return supabase_logout(tokens.auth_token)
        except Exception as e:
            raise Exception(str(e))

    def get_user(self, auth_token: str) -> dict:
        try:
            return supabase_get_user(auth_token)
        except Exception as e:
            raise Exception(str(e))

    def verify_user(self, tokens: AuthTokens) -> dict:
        try:
            return supabase_generate_session(tokens.auth_token, tokens.refresh_token)
        except Exception as e:
            raise Exception(str(e))
