from chalice import Blueprint
from chalicelib.services.profile_service import ProfileService
from chalicelib.models.profile_models import ProfileRequestData
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response

profile_routes = Blueprint(__name__)
profile_service = ProfileService()


@profile_routes.route('/profile', methods=['POST'])
def create_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    try:
        body = ProfileRequestData.parse_obj(request.json_body)
        profile_data = {
            'first_name': body.first_name,
            'last_name': body.last_name,
            'phone': body.phone,
            'dob': body.dob,
        }

        response = profile_service.create_profile_using_function(
            tokens.access_token, profile_data)
        return create_response({
            'profile': response.data['profile'],
            'subscription_card': response.data['subscription_card']
        }, status_code=201)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@profile_routes.route('/profile/me', methods=['GET'])
def get_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    try:
        response = profile_service.get_profile_from_func(tokens.access_token)

        return create_response({
            'profile': response.data['profile'],
            'subscription_card': response.data['subscription_card']
        }, status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@profile_routes.route('/profile/me', methods=['PUT'])
def update_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    try:
        body = ProfileRequestData.parse_obj(request.json_body)
        profile_data = {
            'first_name': body.first_name,
            'last_name': body.last_name,
            'phone': body.phone,
            'dob': body.dob,
        }

        response = profile_service.update_profile(
            tokens.access_token, tokens.refresh_token, profile_data)
        return create_response(response.data[0], status_code=200)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)
