from chalicelib.supabase_module.db_query import insert, get_all, get_by_column, update
from chalicelib.services.auth_service import AuthService
from chalicelib.handlers.get_expire_date_time import get_expire_datetime
from chalicelib.supabase_module.setup_session import setup_session
from chalicelib.services.base_service import BaseService
from chalice import Response


class SubscriptionService(BaseService):
    auth_service = AuthService()

    def get_all_subscription_plans(self):
        try:
            plans = get_all('subscription_programs')
            return Response(body=plans, status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    def get_subscription_plan_by_id(self, id: int):
        try:
            plan = get_by_column('subscription_programs', {'id': id})
            if plan:
                return Response(body=plan, status_code=200)
            return Response(body={'error': 'Plan not found'}, status_code=404)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    def subscribe_to_subscription_plan(self, token: str, refresh: str, request_data: dict):
        setup_session(access_token=token, refresh_token=refresh)
        try:
            user = self.auth_service.get_user(token)
            data = {
                'issued_at': request_data['date'],
                'valid_to': get_expire_datetime(request_data['date']),
                'user_id': user.id,
                'program_id': request_data['program_id']
            }
            insert_result = insert('subscription_cards', data)
            return Response(body={'message': 'Subscription successful', 'data': insert_result}, status_code=201)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    def get_all_user_subscription_cards(self, token: str):
        try:
            user = self.auth_service.get_user(token)
            subscription_cards = get_by_column(
                'subscription_cards', {'user_id': user.id})
            return Response(body=subscription_cards, status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    def get_user_subscription_card_by_id(self, token: str, id: int):
        try:
            user = self.auth_service.get_user(token)
            subscription_card = get_by_column(
                'subscription_cards', {'user_id': user.id, 'id': id})
            if subscription_card:
                return Response(body=subscription_card, status_code=200)
            return Response(body={'error': 'Subscription card not found'}, status_code=404)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    def update_user_subscription_card(self, token: str, id: int, request_data: dict):
        try:
            user = self.auth_service.get_user(token)
            updated_card = update('subscription_cards', {
                                  'id': id, 'user_id': user.id}, request_data)
            if updated_card:
                return Response(body={'message': 'Subscription card updated', 'data': updated_card}, status_code=200)
            return Response(body={'error': 'Subscription card not found or no changes made'}, status_code=404)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
