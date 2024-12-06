from chalicelib.services.subscription_service import SubscriptionService
from chalice import Blueprint

subscription_routes = Blueprint(__name__)
subscription_service = SubscriptionService()


@subscription_routes.route('/subscription-plans', methods=['GET'])
def get_all_subscription_plans():
    return subscription_service.get_all_subscription_plans()


@subscription_routes.route('/subscription-plans/{id}', methods=['GET'])
def get_subscription_plan_by_id(id):
    return subscription_service.get_subscription_plan_by_id(id)


@subscription_routes.route('/subscription-cards', methods=['POST'])
def subscribe_to_subscription_plan():
    request = subscription_routes.current_request  # Correcting the reference
    # Assuming this is for extracting tokens
    tokens = extract_tokens(request.headers)
    auth_token = request.headers['authorization']
    refresh_token = request.headers['refresh']
    request_data = {
        "program_id": request.json_body['program_id'],
        "date": request.json_body['datetime']
    }
    return subscription_service.subscribe_to_subscription_plan(auth_token, refresh_token, request_data)


@subscription_routes.route('/subscription-cards', methods=['GET'])
def get_user_subscription_cards():
    request = subscription_routes.current_request  # Correcting the reference
    auth_token = request.headers['authorization']
    return subscription_service.get_all_user_subscription_cards(auth_token)


@subscription_routes.route('/subscription-cards/{id}', methods=['GET'])
def get_user_subscription_card_by_id(id):
    request = subscription_routes.current_request
    auth_token = request.headers['authorization']
    return subscription_service.get_user_subscription_card_by_id(auth_token, id)


@subscription_routes.route('/subscription-cards/{id}', methods=['PUT'])
def update_user_subscription_card(id):
    request = subscription_routes.current_request
    auth_token = request.headers['authorization']
    request_data = {
        "status": request.json_body['status']
    }
    return subscription_service.update_user_subscription_card(auth_token, id, request_data)
