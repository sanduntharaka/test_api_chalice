from supabase_module.auth import supabase_get_user
from supabase_module.db_query import insert_data, get_all_data, get_data_by_id, update_table_data
from services.auth_service import AuthService


class ProfileService:
    auth_service = AuthService()

    def create_profile(self, token, profile_data):
        user = self.auth_service.get_user(token)
        data = {
            'first_name': profile_data['first_name'],
            'last_name': profile_data['last_name'],
            'email': user.email,
            'phone': profile_data['phone'],
            'dob': profile_data['dob'],
            'user_id': user.id
        }
        return insert_data('user_profile', data)

    def get_profile(self, token):
        user = self.auth_service.get_user(token)
        return get_data_by_id('user_profile', 'user_id', user.id)

    def update_profile(self, token, profile_data):
        user = self.auth_service.get_user(token)
        return update_table_data('user_profile', 'user_id', user.id, profile_data)

    def get_all_profiles(self):
        return get_all_data('user_profile')
