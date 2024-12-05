from chalicelib.supabase_module.auth import supabase_login, supabase_logout, supabase_get_user, supabase_signup, supabase_generate_session
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.models.auth_models import SignUpRequest, LoginRequest, AuthTokens
from typing import Dict


class AuthService:
    def sign_up(self, data: SignUpRequest) -> Dict:
        try:
            # Use Pydantic model's .dict() method to pass data
            response = supabase_signup(data.dict())
            return response
        except Exception as e:
            raise Exception(str(e))

    def login(self, data: LoginRequest) -> AuthTokens:
        try:
            # Use Pydantic model's .dict() method to pass data
            response = supabase_login(data.dict())
            return AuthTokens(
                access_token=response['access_token'],
                refresh_token=response['refresh_token']
            )
        except Exception as e:
            raise Exception(str(e))

    def logout(self, auth_token: str, refresh_token: str) -> Dict:
        try:
            setup_session(access_token=auth_token, refresh_token=refresh_token)
            return supabase_logout(auth_token)
        except Exception as e:
            raise Exception(str(e))

    def get_user(self, auth_token: str) -> Dict:
        print('calling')

        try:
            response = supabase_get_user(auth_token)
            return response
        except Exception as e:
            raise Exception(str(e))

    def verify_user(self, token: str, refresh_token: str) -> Dict:
        try:
            setup_session(access_token=token, refresh_token=refresh_token)
            return supabase_generate_session()
        except Exception as e:
            raise Exception(str(e))
