from supabase_module.db_query import insert, get_all, get_by_column, update
from services.auth_service import AuthService
from handlers.get_expire_date_time import get_expire_datetime


class SubscriptionService:
    auth_service = AuthService()

    def get_all_subscription_plans(self):
        return get_all('subsctiption_programs')

    def get_subscription_plan_by_id(self, id):
        return get_by_column('subsctiption_programs', {'id': id})

    def subscribe_to_subscription_plan(self, token, request_data):
        user = self.auth_service.get_user(token)
        data = {
            'issued_at': request_data['date'],
            'valid_to': get_expire_datetime(request_data['date']),
            'user_id': user.id,
            'program_id': request_data['program_id']
        }

        return insert('subscription_cards', data)

    def get_all_user_subscription_cards(self, token):
        user = self.auth_service.get_user(token)
        return get_by_column('subscription_cards', {'user_id': user.id})

    def get_user_subscription_card_by_id(self, token, id):
        user = self.auth_service.get_user(token)
        return get_by_column('subscription_cards', {'user_id': user.id, 'id': id})

    def update_user_subscription_card(self, token, id, request_data):
        user = self.auth_service.get_user(token)

        return update('subscription_cards', {'id': id, 'user_id': user.id}, request_data)
