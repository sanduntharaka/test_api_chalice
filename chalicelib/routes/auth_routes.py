from chalice import Blueprint
from chalicelib.supabase_module.supabase_config import supabase
from chalicelib.models.auth_models import SignUpRequest, LoginRequest, AuthTokens, GetUserResponse, UserMetadata
from typing import Dict
from chalicelib.services.auth_service import AuthService
from chalicelib.utils.response_helpers import create_response

# Define Blueprint for auth routes
auth_route = Blueprint(__name__)
auth_service = AuthService()


@auth_route.route('/sign-up', methods=['POST'])
def supabase_signup():
    request = auth_route.current_request
    data = SignUpRequest.parse_obj(request.json_body)
    try:
        response = supabase.auth.sign_up(data.dict())
        return create_response({
            'message': 'Sign-up successful',
            'user': {
                'id': response.user.id,
                'email': response.user.user_metadata['email'],
                'provider': response.user.app_metadata['provider'],
            }
        }, status_code=201)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@auth_route.route('/login', methods=['POST'])
def supabase_login():
    request = auth_route.current_request
    data = LoginRequest.parse_obj(request.json_body)

    try:
        response = supabase.auth.sign_in_with_password(data.dict())
        return create_response({
            'access_token': response.session.access_token,
            'refresh_token': response.session.refresh_token
        }, status_code=200)

    except Exception as e:
        return create_response({'error': str(e), 'message': 'Error during login'}, status_code=400)


@auth_route.route('/logout', methods=['POST'])
def supabase_logout():
    request = auth_route.current_request
    auth_token = request.headers.get('authorization', None)

    if not auth_token:
        return create_response({'error': 'Authorization token missing', 'message': 'Error logging out'}, status_code=400)

    try:
        supabase.auth.sign_out()
        return create_response({'message': 'Logged out successfully'}, status_code=200)
    except Exception as e:
        return create_response({'error': str(e), 'message': 'Error logging out'}, status_code=400)


@auth_route.route('/get-user', methods=['GET'])
def supabase_get_user():
    request = auth_route.current_request
    auth_token = request.headers.get('authorization', None)

    if not auth_token:
        return create_response({'error': 'Authorization token missing', 'message': 'Error fetching user'}, status_code=400)

    try:
        response = supabase.auth.get_user(auth_token)
        user = response.user
        return create_response({
            'detail': 'User verified',
            'data': UserMetadata(
                user_id=user.id,
                provider=user.app_metadata['provider'],
                email=user.user_metadata['email']
            ).dict()
        }, status_code=200)
    except Exception as e:
        return create_response({'error': str(e), 'message': 'Error fetching user'}, status_code=400)


@auth_route.route('/verify', methods=['GET'])
def supabase_verify_user():
    request = auth_route.current_request
    auth_token = request.headers.get('authorization', None)
    refresh_token = request.headers.get('refresh', None)

    if not auth_token or not refresh_token:
        return create_response({'error': 'Authorization or refresh token missing', 'message': 'Error verifying user'}, status_code=400)

    try:
        response = supabase.auth.refresh_session(auth_token)
        return create_response({
            'message': 'User verified',
            'session': response.json()
        }, status_code=200)
    except Exception as e:
        return create_response({'error': str(e), 'message': 'Error verifying user'}, status_code=400)
