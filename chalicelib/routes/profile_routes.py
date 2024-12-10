from chalice import Blueprint
from chalicelib.services.profile_service import ProfileService
from chalicelib.models.profile_models import ProfileRequestData, ProfileUpdateRequestData
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response
from chalicelib.decorators.handle_exceptions import handle_exceptions
profile_routes = Blueprint(__name__)
profile_service = ProfileService()


@profile_routes.route('/profile', methods=['POST'])
@handle_exceptions
def create_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    body = ProfileRequestData.parse_obj(request.json_body)

    response = profile_service.create_profile_using_function(
        tokens.access_token, body)
    return create_response({
        'profile': response.data['profile'],
        'subscription_card': response.data['subscription_card']
    }, status_code=201)


@profile_routes.route('/profile/me', methods=['GET'])
@handle_exceptions
def get_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    response = profile_service.get_profile_from_func(tokens.access_token)

    return create_response({
        'profile': response.data['profile'],
        'subscription_card': response.data['subscription_card']
    }, status_code=200)


@profile_routes.route('/profile/me', methods=['PUT'])
@handle_exceptions
def update_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    body = ProfileUpdateRequestData.parse_obj(request.json_body)
    profile_data = {
        'first_name': body.first_name,
        'last_name': body.last_name,
        'phone': body.phone,
        'dob': body.dob,
    }

    response = profile_service.update_profile(
        tokens.access_token, tokens.refresh_token, profile_data)
    return create_response(response.data[0], status_code=200)
