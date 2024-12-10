from chalice import Blueprint
from chalicelib.supabase_module.supabase_config import supabase
from chalicelib.models.auth_models import SignUpRequest, LoginRequest, AuthTokens, GetUserResponse, UserMetadata
from chalicelib.decorators.handle_exceptions import handle_exceptions
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.services.auth_service import AuthService
from chalicelib.utils.response_helpers import create_response

# Define Blueprint for auth routes
auth_route = Blueprint(__name__)
auth_service = AuthService()


@auth_route.route('/sign-up', methods=['POST'])
@handle_exceptions
def supabase_signup():
    request = auth_route.current_request
    data = SignUpRequest.parse_obj(request.json_body)
    response = auth_service.sign_up(data)
    return create_response({
        'message': 'Sign-up successful',
        'user': {
            'id': response.user.id,
            'email': response.user.user_metadata['email'],
            'provider': response.user.app_metadata['provider'],
        }
    }, status_code=201)


@auth_route.route('/login', methods=['POST'])
@handle_exceptions
def supabase_login():
    request = auth_route.current_request
    data = LoginRequest.parse_obj(request.json_body)

    response = auth_service.login(data)
    return create_response(response, status_code=200)


@auth_route.route('/logout', methods=['POST'])
@handle_exceptions
def supabase_logout():
    request = auth_route.current_request
    tokens = extract_tokens(request.headers)
    response = auth_service.logout(
        tokens.access_token, tokens.refresh_token)
    return create_response(response, status_code=200)


@auth_route.route('/get-user', methods=['GET'])
@handle_exceptions
def supabase_get_user():
    request = auth_route.current_request
    tokens = extract_tokens(request.headers)

    response = auth_service.get_user(tokens.access_token)
    return create_response({
        'detail': 'User verified',
        'data': UserMetadata(
            user_id=response.id,
            provider=response.app_metadata['provider'],
            email=response.email
        ).model_dump()
    }, status_code=200)


@auth_route.route('/verify', methods=['GET'])
@handle_exceptions
def supabase_verify_user():
    request = auth_route.current_request
    tokens = extract_tokens(request.headers)

    response = auth_service.verify_user(
        tokens.access_token, tokens.refresh_token)
    return create_response({
        "access_token": response.session.access_token,
        "refresh_token": response.session.refresh_token
    }, status_code=200)
