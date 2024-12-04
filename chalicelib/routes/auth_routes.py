from chalice import Blueprint, Response
from chalicelib.services.auth_service import AuthService
from chalicelib.models.auth_models import SignUpRequest, LoginRequest
from chalicelib.utils.response_helpers import create_response
from chalicelib.utils.token_utils import extract_tokens

auth_routes = Blueprint(__name__)
auth_service = AuthService()


@auth_routes.route('/sign-up', methods=['POST'])
def sign_up():
    request = auth_routes.current_request
    body = SignUpRequest.parse_obj(request.json_body)
    try:
        response = auth_service.sign_up(body.email, body.password)
        return create_response({
            'detail': 'email verification link sent',
            'data': response
        })
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@auth_routes.route('/login', methods=['POST'])
def login():
    request = auth_routes.current_request
    body = LoginRequest.parse_obj(request.json_body)
    try:
        return create_response(auth_service.login(body.email, body.password))
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@auth_routes.route('/logout', methods=['POST'])
def logout():
    tokens = extract_tokens(auth_routes.current_request.headers)
    try:
        return create_response(auth_service.logout(tokens))
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@auth_routes.route('/get-user', methods=['GET'])
def get_user():
    tokens = extract_tokens(auth_routes.current_request.headers)
    try:
        user = auth_service.get_user(tokens['auth_token'])
        return create_response({
            'detail': 'user verified',
            'data': user
        })
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)


@auth_routes.route('/verify', methods=['GET'])
def verify_user():
    tokens = extract_tokens(auth_routes.current_request.headers)
    try:
        response = auth_service.verify_user(tokens)
        return create_response(response)
    except Exception as e:
        return create_response({'error': str(e)}, status_code=400)
