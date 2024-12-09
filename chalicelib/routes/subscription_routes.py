from chalicelib.services.subscription_service import SubscriptionService
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response

from chalice import Blueprint

subscription_routes = Blueprint(__name__)
subscription_service = SubscriptionService()


@subscription_routes.route('/subscription-plans', methods=['GET'])
def get_all_subscription_plans():
    try:
        response = subscription_service.get_all_subscription_plans()
        return create_response(response, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@subscription_routes.route('/subscription-plans/{id}', methods=['GET'])
def get_subscription_plan_by_id(id):
    try:
        response = subscription_service.get_subscription_plan_by_id(id)
        return create_response(response, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@subscription_routes.route('/subscription-cards', methods=['POST'])
def subscribe_to_subscription_plan():
    request = subscription_routes.current_request  # Correcting the reference
    # Assuming this is for extracting tokens
    tokens = extract_tokens(request.headers)
    request_data = {
        "program_id": request.json_body['program_id'],
        "date": request.json_body['datetime']
    }
    try:
        response = subscription_service.subscribe_to_subscription_plan(
            tokens.access_token, tokens.refresh_token, request_data)
        return create_response(response, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@subscription_routes.route('/subscription-cards', methods=['GET'])
def get_user_subscription_cards():
    request = subscription_routes.current_request  # Correcting the reference
    tokens = extract_tokens(request.headers)

    try:
        response = subscription_service.get_all_user_subscription_cards(
            tokens.access_token)
        return create_response(response, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@subscription_routes.route('/subscription-cards/{id}', methods=['GET'])
def get_user_subscription_card_by_id(id):
    request = subscription_routes.current_request
    tokens = extract_tokens(request.headers)

    try:
        response = subscription_service.get_user_subscription_card_by_id(
            tokens.access_token, id)
        return create_response(response, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@subscription_routes.route('/subscription-cards/{id}', methods=['PUT'])
def update_user_subscription_card(id):
    request = subscription_routes.current_request
    tokens = extract_tokens(request.headers)

    request_data = {
        "status": request.json_body['status']
    }
    try:
        response = subscription_service.update_user_subscription_card(
            tokens.access_token, id, request_data)
        return create_response(response, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)
