from chalicelib.supabase_module.auth import supabase_login, supabase_logout, supabase_get_user, supabase_signup, supabase_generate_session
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.models.auth_models import SignUpRequest, LoginRequest, AuthTokens, GetUserResponse, UserMetadata
from typing import Dict
from chalicelib.supabase_module.supabase_config import supabase


class AuthService:
    # def sign_up(self, data: SignUpRequest) -> Dict:
    #     try:
    #         response = supabase_signup(data.dict())
    #         return response
    #     except Exception as e:
    #         raise Exception(str(e))

    def sign_up(self, request_data: dict) -> Dict:
        try:
            data = SignUpRequest.parse_obj(request_data)
            response = supabase.auth.supabase_signup(data.dict())

            return {
                'message': 'Sign-up successful',
                'user': {
                    'id': response.user.id,
                    'email': response.user.user_metadata['email'],
                    'provider': response.user.app_metadata['provider'],
                }
            }
        except Exception as e:
            raise Exception(str(e))

    # def login(self, data: LoginRequest) -> AuthTokens:
    #     try:
    #         response = supabase_login(data.dict())
    #         return AuthTokens(
    #             access_token=response['access_token'],
    #             refresh_token=response['refresh_token']
    #         )
    #     except Exception as e:
    #         raise Exception(str(e))

    def login(self, request_data: dict) -> AuthTokens:
        try:
            data = LoginRequest.parse_obj(request_data)
            response = supabase.auth.supabase_login(data.dict())

            return AuthTokens(
                access_token=response.session.access_token,
                refresh_token=response.session.refresh_token
            )
        except Exception as e:
            raise Exception(f"Login Error: {str(e)}")

    # def logout(self, auth_token: str, refresh_token: str) -> Dict:
    #     try:
    #         setup_session(access_token=auth_token, refresh_token=refresh_token)
    #         return supabase_logout(auth_token)
    #     except Exception as e:
    #         raise Exception(str(e))

    def logout(self, auth_token: str, refresh_token: str) -> Dict:
        try:
            setup_session(access_token=auth_token, refresh_token=refresh_token)

            supabase.auth.supabase_logout()

            return {
                'message': 'Logged out successfully'
            }
        except Exception as e:
            raise Exception(f"Error logging out: {str(e)}")

    # def get_user(self, auth_token: str) -> Dict:

    #     try:
    #         response = supabase_get_user(auth_token)
    #         return response
    #     except Exception as e:
    #         raise Exception(str(e))

    def get_user(self, auth_token: str) -> Dict:
        try:
            response = supabase.auth.supabase_get_user(auth_token)
            user = response.user

            return {
                'detail': 'User verified',
                'data': UserMetadata(
                    user_id=user.id,
                    provider=user.app_metadata['provider'],
                    email=user.user_metadata['email']
                ).dict()
            }
        except Exception as e:
            raise Exception(f"Error fetching user: {str(e)}")

    # def verify_user(self, token: str, refresh_token: str) -> Dict:
    #     try:
    #         setup_session(access_token=token, refresh_token=refresh_token)
    #         return supabase_generate_session()
    #     except Exception as e:
    #         raise Exception(str(e))

    def verify_user(self, access_token: str, refresh_token: str) -> Dict:
        try:
            setup_session(access_token=access_token,
                          refresh_token=refresh_token)

            response = supabase.auth.supabase_generate_session(access_token)

            return {
                'message': 'User verified',
                'session': response.json()
            }
        except Exception as e:
            raise Exception(f"Error verifying user: {str(e)}")
