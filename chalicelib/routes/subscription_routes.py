from chalicelib.services.subscription_service import SubscriptionService
from chalicelib.models.subscriptionPlan_model import CreateSubscriptionCard, UpdateSubscriptionCard
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response
from chalicelib.decorators.handle_exceptions import handle_exceptions
from chalicelib.config import cors_config

from chalice import Blueprint
subscription_routes = Blueprint(__name__)
subscription_service = SubscriptionService()


@subscription_routes.route('/subscription-plans', methods=['GET'], cors=cors_config)
@handle_exceptions
def get_all_loyalty_programs():
    response = subscription_service.get_all_subscription_plans()
    return create_response(response, status_code=200)


@subscription_routes.route('/subscription-plans/{id}', methods=['GET'], cors=cors_config)
@handle_exceptions
def get_loyalty_program_by_id(id):
    response = subscription_service.get_subscription_plan_by_id(id)
    return create_response(response, status_code=200)


@subscription_routes.route('/subscription-cards', methods=['POST'], cors=cors_config)
@handle_exceptions
def subscribe_to_loyalty_program():
    request = subscription_routes.current_request
    tokens = extract_tokens(request.headers)
    body = CreateSubscriptionCard.model_validate(request.json_body)
    response = subscription_service.subscribe_to_subscription_plan(
        tokens.access_token, tokens.refresh_token, body)
    return create_response(response, status_code=201)


@subscription_routes.route('/subscription-cards', methods=['GET'], cors=cors_config)
@handle_exceptions
def get_user_loyalty_cards():
    request = subscription_routes.current_request
    tokens = extract_tokens(request.headers)
    response = subscription_service.get_all_user_subscription_cards(
        tokens.access_token)
    return create_response(response, status_code=200)


@subscription_routes.route('/subscription-cards/{id}', methods=['GET'], cors=cors_config)
@handle_exceptions
def get_user_loyalty_card_by_id(id):
    request = subscription_routes.current_request
    tokens = extract_tokens(request.headers)
    response = subscription_service.get_user_subscription_card_by_id(
        tokens.access_token, id)
    return create_response(response, status_code=200)


@subscription_routes.route('/subscription-cards/{id}', methods=['PUT'], cors=cors_config)
def get_user_loyalty_card_by_id(id):
    request = subscription_routes.current_request
    tokens = extract_tokens(request.headers)
    body = UpdateSubscriptionCard.model_validate(request.json_body)
    response = subscription_service.update_user_subscription_card(
        tokens.access_token, id, body)
    return create_response(response.model_dump_json(), status_code=200)
