from chalicelib.supabase_module.db_query import insert, get_all, get_by_column, update, call_function
from chalicelib.services.auth_service import AuthService
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.services.base_service import BaseService
from chalice import Response

import json


class ProfileService(BaseService):
    auth_service = AuthService()

    def create_profile_using_function(self, token, profile_data):
        user = self.get_user_details(token)
        data = {
            'first_name': profile_data['first_name'],
            'last_name': profile_data['last_name'],
            'email': user.email,
            'phone': profile_data['phone'],
            'dob': profile_data['dob'],
            'user_id': user.id
        }

        created_data = call_function(
            'create_profile_and_get_subscription', data)
        return created_data

    def get_profile_from_func(self, token):
        user = self.get_user_details(token)
        data = {
            'user_id': user.id
        }

        profile_data = call_function(
            'get_user_profile_with_subscription', data)
        return profile_data

    def update_profile(self, token, refresh, profile_data):
        setup_session(access_token=token, refresh_token=refresh)

        user = self.auth_service.get_user(token)

        profile_data['user_id'] = user.id
        return update('user_profile', {'user_id': user.id}, profile_data)

    def get_all_profiles(self):
        return get_all('user_profile')
