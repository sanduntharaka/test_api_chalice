from chalicelib.supabase_module.db_query import insert, get_by_column
from chalicelib.handlers.get_expire_date_time import get_expire_datetime
import json


# def create_subscription_card(data):
#     """
#     if program_id is empty, return the last subscription card id
#     else, check if user has subscription card, if not, create new subscription card
#     """
#     check_subscription = json.loads(get_by_column(
#         'subscription_cards', {'user_id': data['user_id']}))

#     if data['program_id'] == "":
#         if len(check_subscription['data']) == 0:
#             raise Exception('User has no subscription card')
#         return check_subscription['data'][-1]['id']
#     else:
#         if len(check_subscription['data']) > 0:
#             return check_subscription['data'][-1]['id']
#         else:
#             data['valid_to'] = get_expire_datetime(data['issued_at'])

#             response = json.loads(insert('subscription_cards', data))
#             return response['data'][0]['id']


def create_subscription_card(data):
    """
    Create or retrieve a subscription card for a user based on the program_id.
    """
    # Fetch existing subscription cards for the user
    check_subscription = json.loads(get_by_column(
        'subscription_cards', {'user_id': data['user_id']}))
    existing_cards = check_subscription.get('data', [])

    # If program_id is empty, return the last subscription card ID if it exists
    if not data['program_id']:
        return _handle_empty_program_id(existing_cards)

    # If program_id is provided, check for existing cards or create a new one
    return _handle_with_program_id(existing_cards, data)


def _handle_empty_program_id(existing_cards):
    """
    Handle case when program_id is empty.
    """
    if not existing_cards:
        raise Exception('User has no subscription card')
    return existing_cards[-1]['id']


def _handle_with_program_id(existing_cards, data):
    """
    Handle case when program_id is provided.
    """
    if existing_cards:
        return existing_cards[-1]['id']

    # Create a new subscription card
    data['valid_to'] = get_expire_datetime(data['issued_at'])
    response = json.loads(insert('subscription_cards', data))
    return response['data'][0]['id']
