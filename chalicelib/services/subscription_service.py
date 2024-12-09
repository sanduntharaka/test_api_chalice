from chalicelib.supabase_module.db_query import insert, get_all, get_by_column, update
from chalicelib.handlers.get_expire_date_time import get_expire_datetime
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.services.base_service import BaseService


class SubscriptionService(BaseService):

    def get_all_subscription_plans(self):
        try:
            plans = get_all('subscription_programs')
            return plans
        except Exception as e:
            raise Exception(str(e))

    def get_subscription_plan_by_id(self, id: int):
        try:
            plan = get_by_column('subscription_programs', {'id': id})

            return plan
        except Exception as e:
            raise Exception(str(e))

    def subscribe_to_subscription_plan(self, token: str, refresh: str, request_data: dict):
        setup_session(access_token=token, refresh_token=refresh)
        try:
            user = self.get_user_details(token)  # Use BaseService's method
            data = {
                'issued_at': request_data['date'],
                'valid_to': get_expire_datetime(request_data['date']),
                # Ensure `user` has the required attributes
                'user_id': user['id'],
                'program_id': request_data['program_id']
            }
            insert_result = insert('subscription_cards', data)
            return insert_result
        except Exception as e:
            raise Exception(str(e))

    def get_all_user_subscription_cards(self, token: str):
        try:
            user = self.get_user_details(token)  # Use BaseService's method
            subscription_cards = get_by_column(
                'subscription_cards', {'user_id': user['id']}
            )
            return subscription_cards
        except Exception as e:
            raise Exception(str(e))

    def get_user_subscription_card_by_id(self, token: str, id: int):
        try:
            user = self.get_user_details(token)  # Use BaseService's method
            subscription_card = get_by_column(
                'subscription_cards', {'user_id': user['id'], 'id': id}
            )
            return subscription_card
        except Exception as e:
            raise Exception(str(e))

    def update_user_subscription_card(self, token: str, id: int, request_data: dict):
        try:
            user = self.get_user_details(token)  # Use BaseService's method
            updated_card = update(
                'subscription_cards', {
                    'id': id, 'user_id': user['id']}, request_data
            )
            return updated_card
        except Exception as e:
            raise Exception(str(e))
