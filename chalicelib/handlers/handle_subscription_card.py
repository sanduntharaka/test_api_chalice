from chalicelib.supabase_module.db_query import insert, get_by_column
from chalicelib.handlers.get_expire_date_time import get_expire_datetime
import json


def create_subscription_card(data):
    """
    if program_id is empty, return the last subscription card id
    else, check if user has subscription card, if not, create new subscription card
    """
    check_subscription = json.loads(get_by_column(
        'subscription_cards', {'user_id': data['user_id']}))

    if data['program_id'] == "":
        if len(check_subscription['data']) == 0:
            raise Exception('User has no subscription card')
        return check_subscription['data'][-1]['id']
    else:
        if len(check_subscription['data']) > 0:
            return check_subscription['data'][-1]['id']
        else:
            data['valid_to'] = get_expire_datetime(data['issued_at'])

            response = json.loads(insert('subscription_cards', data))
            return response['data'][0]['id']
