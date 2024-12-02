from chalicelib.supabase_module.db_query import insert, get_all, get_by_column, update
from chalicelib.services.auth_service import AuthService
from chalicelib.supabase_module.setup_session import setup_session
from chalice import Response

import json


class ProfileService:
    auth_service = AuthService()

    def create_profile(self, token, profile_data):
        try:
            user = self.auth_service.get_user(token)
            print(user)
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

        created_data = json.loads(insert('user_profile', data))
        card_data = json.loads(get_by_column(
            'subscription_cards', {'user_id': user.id}))
        data = {
            'profile': created_data['data'],
            'subscription_card': card_data['data']
        }
        return data

    def get_profile(self, token):
        try:
            user = self.auth_service.get_user(token)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

        profile_data = json.loads(get_by_column(
            'user_profile', {'user_id': user.id}))
        card_data = json.loads(get_by_column(
            'subscription_cards', {'user_id': user.id}))

        data = {
            'profile': profile_data['data'],
            'subscription_card': card_data['data']
        }
        return data

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

# TODO check in supabase and create db function to create and get user
