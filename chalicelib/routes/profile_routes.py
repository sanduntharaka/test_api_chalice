from chalice import Blueprint
from chalicelib.services.profile_service import ProfileService
from chalicelib.models.profile_models import ProfileRequestData, ProfileResponseData
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response

profile_routes = Blueprint(__name__)
profile_service = ProfileService()


@profile_routes.route('/profile', methods=['POST'])
def create_user_profile():
    request = profile_routes.current_request
    tokens = extract_tokens(request.headers)
    try:
        print('hi')
        body = ProfileRequestData.parse_obj(request.json_body)
        profile_data = {
            'first_name': body.first_name,
            'last_name': body.last_name,
            'phone': body.phone,
            'dob': body.dob,
        }

        response = profile_service.create_profile_using_function(
            tokens.access_token, profile_data)
        print("rr:", response.data['profile'])

        response = ProfileResponseData(
            profile=response.data['profile'],
            subscription_card=response.data['subscription_card']
        )
        print("rrqq:", response)
        return create_response(response.model_dump())
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@profile_routes.route('/profile/me', methods=['GET'])
def get_user_profile():
    request = profile_routes.current_request
    auth_token = request.headers['authorization']
    return profile_service.get_profile(auth_token)


@profile_routes.route('/profile/me', methods=['PUT'])
def update_user_profile():
    request = profile_routes.current_request
    auth_token = request.headers['authorization']
    refresh_token = request.headers['refresh']
    profile_data = {
        'first_name': request.json_body['first_name'],
        'last_name': request.json_body['last_name'],
        'phone': request.json_body['phone'],
        'dob': request.json_body['dob'],
    }
    return profile_service.update_profile(auth_token, refresh_token, profile_data)
