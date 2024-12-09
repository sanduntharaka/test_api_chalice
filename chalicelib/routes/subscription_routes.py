from chalicelib.services.subscription_service import SubscriptionService
from chalice import Blueprint
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response

subscription_routes = Blueprint(__name__)
subscription_service = SubscriptionService()


# @subscription_routes.route('/subscription-plans', methods=['GET'])
# def get_all_subscription_plans():
#     return subscription_service.get_all_subscription_plans()

@subscription_routes.route('/subscription-plans', methods=['GET'])
def get_all_subscription_plans():
    try:
        response = subscription_service.get_all_subscription_plans()

        if 'error' in response:
            return create_response({'error': response['error'], 'message': response.get('message', 'Error fetching subscription plans')}, status_code=404)

        return create_response({'message': response['message'], 'data': response['data']}, status_code=200)
    except Exception as e:
        return create_response(
            {
                'error': str(e),
                'message': 'Unexpected error occurred while fetching subscription plans'
            },
            status_code=500
        )


# @subscription_routes.route('/subscription-plans/{id}', methods=['GET'])
# def get_subscription_plan_by_id(id):
#     return subscription_service.get_subscription_plan_by_id(id)

@subscription_routes.route('/subscription-plans/{id}', methods=['GET'])
def get_subscription_plan_by_id(id):
    try:
        response = subscription_service.get_subscription_plan_by_id(int(id))

        if 'error' in response:
            status_code = 404 if response['error'] == 'Plan not found' else 400
            return create_response(response, status_code=status_code)

        return create_response(response, status_code=200)
    except Exception as e:
        return create_response(
            {'error': str(e), 'message': 'Error fetching subscription plan'},
            status_code=500
        )


# @subscription_routes.route('/subscription-cards', methods=['POST'])
# def subscribe_to_subscription_plan():
#     request = subscription_routes.current_request  # Correcting the reference
#     tokens = extract_tokens(request.headers)
#     request_data = {
#         "program_id": request.json_body['program_id'],
#         "date": request.json_body['datetime']
#     }
#     return subscription_service.subscribe_to_subscription_plan(tokens.access_token, tokens.refresh_token, request_data)

@subscription_routes.route('/subscription-cards', methods=['POST'])
def subscribe_to_subscription_plan():
    try:
        request = subscription_routes.current_request
        tokens = extract_tokens(request.headers)

        if not tokens.access_token or not tokens.refresh_token:
            return create_response(
                {
                    'error': 'Authorization or refresh token missing',
                    'message': 'Cannot proceed without valid tokens'
                },
                status_code=400
            )

        request_data = {
            'program_id': request.json_body['program_id'],
            'date': request.json_body['datetime']
        }

        response = subscription_service.subscribe_to_subscription_plan(
            token=tokens.access_token,
            refresh_token=tokens.refresh_token,
            request_data=request_data
        )

        if 'error' in response:
            return create_response(
                {
                    'error': response['error'],
                    'message': response['message']
                },
                status_code=400
            )

        return create_response(
            {
                'message': response['message'],
                'data': response['data']
            },
            status_code=201
        )
    except Exception as e:
        return create_response(
            {
                'error': str(e),
                'message': 'Unexpected error occurred while subscribing to the subscription plan'
            },
            status_code=500
        )


# @subscription_routes.route('/subscription-cards', methods=['GET'])
# def get_user_subscription_cards():
#     request = subscription_routes.current_request  # Correcting the reference
#     tokens = extract_tokens(request.headers)
#     return subscription_service.get_all_user_subscription_cards(tokens)

@subscription_routes.route('/subscription-cards', methods=['GET'])
def get_user_subscription_cards():
    try:
        # Get the request object
        request = subscription_routes.current_request

        # Extract tokens from headers
        tokens = extract_tokens(request.headers)

        # Ensure tokens are valid
        if not tokens.access_token or not tokens.refresh_token:
            return create_response(
                {
                    'error': 'Authorization or refresh token missing',
                    'message': 'Cannot proceed without valid tokens'
                },
                status_code=400
            )

        response = subscription_service.get_all_user_subscription_cards(
            tokens.access_token)

        if 'error' in response:
            return create_response(
                {
                    'error': response['error'],
                    'message': response['message']
                },
                status_code=400
            )

        return create_response(
            {
                'message': response['message'],
                'data': response['data']
            },
            status_code=200
        )
    except Exception as e:
        return create_response(
            {
                'error': str(e),
                'message': 'Unexpected error occurred while fetching subscription cards'
            },
            status_code=500
        )


# @subscription_routes.route('/subscription-cards/{id}', methods=['GET'])
# def get_user_subscription_card_by_id(id):
#     request = subscription_routes.current_request
#     tokens = extract_tokens(request.headers)
#     return subscription_service.get_user_subscription_card_by_id(tokens, id)

@subscription_routes.route('/subscription-cards/{id}', methods=['GET'])
def get_user_subscription_card_by_id(id):
    try:
        request = subscription_routes.current_request
        tokens = extract_tokens(request.headers)

        if not tokens.access_token or not tokens.refresh_token:
            return create_response(
                {
                    'error': 'Authorization or refresh token missing',
                    'message': 'Cannot proceed without valid tokens'
                },
                status_code=400
            )

        response = subscription_service.get_user_subscription_card_by_id(
            tokens.access_token, id)

        if 'error' in response:
            return create_response(
                {
                    'error': response['error'],
                    'message': response['message']
                },
                status_code=404 if 'not found' in response['error'].lower(
                ) else 400
            )

        return create_response(
            {
                'message': response['message'],
                'data': response['data']
            },
            status_code=200
        )
    except Exception as e:
        return create_response(
            {
                'error': str(e),
                'message': 'Unexpected error occurred while fetching subscription card'
            },
            status_code=500
        )


# @subscription_routes.route('/subscription-cards/{id}', methods=['PUT'])
# def update_user_subscription_card(id):
#     request = subscription_routes.current_request
#     tokens = extract_tokens(request.headers)
#     request_data = {
#         "status": request.json_body['status']
#     }
#     return subscription_service.update_user_subscription_card(tokens, id, request_data)

@subscription_routes.route('/subscription-cards/{id}', methods=['PUT'])
def update_user_subscription_card(id):
    try:
        request = subscription_routes.current_request
        tokens = extract_tokens(request.headers)

        if not tokens.access_token or not tokens.refresh_token:
            return create_response(
                {
                    'error': 'Authorization or refresh token missing',
                    'message': 'Cannot proceed without valid tokens'
                },
                status_code=400
            )

        request_data = {
            "status": request.json_body['status']
        }

        response = subscription_service.update_user_subscription_card(
            tokens.access_token, id, request_data)

        if 'error' in response:
            return create_response(
                {
                    'error': response['error'],
                    'message': response['message']
                },
                status_code=404 if 'not found' in response['error'].lower(
                ) else 400
            )

        return create_response(
            {
                'message': response['message'],
                'data': response['data']
            },
            status_code=200
        )
    except Exception as e:
        return create_response(
            {
                'error': str(e),
                'message': 'Unexpected error occurred while updating subscription card'
            },
            status_code=500
        )
