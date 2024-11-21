from supabase_module.db_query import insert, get_all, get_by_column, update
from services.auth_service import AuthService
from supabase_module.setup_session import setup_session
from chalice import Response


class ProfileService:
    auth_service = AuthService()

    def create_profile(self, token, profile_data):
        try:
            user = self.auth_service.get_user(token)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
        data = {
            'first_name': profile_data['first_name'],
            'last_name': profile_data['last_name'],
            'email': user.email,
            'phone': profile_data['phone'],
            'dob': profile_data['dob'],
            'user_id': user.id
        }
        return insert('user_profile', data)

    def get_profile(self, token):
        try:
            user = self.auth_service.get_user(token)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
        return get_by_column('user_profile', {'user_id': user.id})

    def update_profile(self, token, refresh, profile_data):
        setup_session(access_token=token, refresh_token=refresh)

        try:
            user = self.auth_service.get_user(token)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
        # print(user.refresh_token)
        profile_data['user_id'] = user.id
        return update('user_profile', {'user_id': user.id}, profile_data)

    def get_all_profiles(self):
        return get_all('user_profile')
