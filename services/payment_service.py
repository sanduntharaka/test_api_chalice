from supabase_module.db_query import insert, get_by_column, filter_by_range, call_function
from services.auth_service import AuthService
from datetime import datetime, timedelta
from handlers.handle_subscription_card import create_subscription_card
# from handlers.handle_top_up import add_top_to_subscription_card
from supabase_module.setup_session import setup_session


class PaymentService:
    auth_service = AuthService()

    def get_all_payments(self, token):
        user = self.auth_service.get_user(token)
        return get_by_column('user_payments', {'user_id': user.id})

    def add_payment(self, token, request_data):
        user = self.auth_service.get_user(token)
        if request_data['type'] == 'subscription':
            # create subscription card if not then top up
            data = {
                'issued_at': request_data['date_time'],
                'user_id': user.id,
                'program_id': request_data['program_id']
            }

            card_id = create_subscription_card(data)

        # if request_data['type'] == 'top-up':
        #     # top up
        #     data = {
        #         'issued_at': request_data['date_time'],
        #         'user_id': user.id
        #     }
        #     card_id =

        data = {
            'user_id': user.id,
            'amount': request_data['amount'],
            'type': request_data['type'],
            'status': 'success',
            'payment_date': request_data['date_time'],
            'subscription_card': card_id
        }

        return insert('user_payments', data)

    def filter_payments_by_date_range(self, token, refresh, start_date, end_date):
        setup_session(access_token=token, refresh_token=refresh)
        user = self.auth_service.get_user(token)
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        return filter_by_range('user_payments', {'user_id': user.id}, {'column': "payment_date", "start": start_date, 'end': end_date})

    def test_payment(self, token):
        user = self.auth_service.get_user(token)
        return call_function('calculate_total_subscription', {"user_id": user.id, "amount": 2})
