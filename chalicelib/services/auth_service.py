from chalicelib.supabase_module.auth import supabase_login, supabase_logout, supabase_get_user, supabase_signup, supabase_generate_session
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.models.auth_models import SignUpRequest, LoginRequest, AuthTokens
from typing import Dict


class AuthService:
    def sign_up(self, data: SignUpRequest) -> Dict:
        response = supabase_signup(data.model_dump())
        return response

    def login(self, data: LoginRequest) -> AuthTokens:
        response = supabase_login(data.model_dump())
        return response

    def logout(self, auth_token: str, refresh_token: str) -> Dict:
        setup_session(access_token=auth_token, refresh_token=refresh_token)
        return supabase_logout()

    def get_user(self, auth_token: str) -> Dict:
        response = supabase_get_user(auth_token)
        return response

    def verify_user(self, token: str, refresh_token: str) -> Dict:
        setup_session(access_token=token, refresh_token=refresh_token)
        return supabase_generate_session()
