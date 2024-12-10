from chalicelib.supabase_module.db_query import insert, get_all, get_by_column, update
from chalicelib.services.auth_service import AuthService
from chalicelib.handlers.get_expire_date_time import get_expire_datetime
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.services.base_service import BaseService

from chalice import Response


class SubscriptionService(BaseService):

    def get_all_subscription_plans(self):
        return get_all('subscription_programs')

    def get_subscription_plan_by_id(self, id):
        return get_by_column('subscription_programs', {'id': id})

    def subscribe_to_subscription_plan(self, token, refresh, request_data):
        setup_session(access_token=token, refresh_token=refresh)

        user = self.get_user_details(token)
        data = {
            'issued_at': str(request_data.datetime),
            'valid_to': get_expire_datetime(str(request_data.datetime)),
            'user_id': user.id,
            'program_id': request_data.program_id,
        }

        return insert('subscription_cards', data)

    def get_all_user_subscription_cards(self, token):
        user = self.get_user_details(token)

        return get_by_column('subscription_cards', {'user_id': user.id})

    def get_user_subscription_card_by_id(self, token, id):
        user = self.get_user_details(token)

        return get_by_column('subscription_cards', {'user_id': user.id, 'id': id})

    def update_user_subscription_card(self, token, id, request_data):
        user = self.get_user_details(token)
        print(request_data.model_dump())
        return update('subscription_cards', {'id': id, 'user_id': user.id}, request_data.model_dump())
