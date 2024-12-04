from chalicelib.services.auth_service import AuthService
from chalice import Response
import json


def create_auth_routes(app):
    auth_service = AuthService()

    @app.route('/sign-up', methods=['POST'])
    def sign_up():
        request = app.current_request
        email = request.json_body['email']
        password = request.json_body['password']
        try:
            response = auth_service.sign_up(email, password)
            return Response(body={
                'detail': 'email verification link sent',
                'data': {
                    'id': response.user.id,
                    'provider': response.user.app_metadata['provider'],
                    'email': response.user.user_metadata['email']

                }
            }, status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    @app.route('/login', methods=['POST'])
    def login():
        request = app.current_request
        email = request.json_body['email']
        password = request.json_body['password']

        try:
            return Response(body=auth_service.login(email, password), status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    @app.route('/logout', methods=['POST'])
    def logout():
        request = app.current_request
        auth_token = request.headers['authorization']
        refresh_token = request.headers['refresh']

        try:
            return Response(body=auth_service.logout(auth_token, refresh_token), status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    @app.route('/get-user', methods=['GET'])
    def get_user():
        request = app.current_request
        auth_token = request.headers['authorization']
        try:
            user = auth_service.get_user(auth_token)
            return Response(body={
                'detail': 'user verified',
                'data': {
                    'user_id': user.id,
                    'provider': user.app_metadata['provider'],
                    'email': user.user_metadata['email']
                }

            }, status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)

    @app.route('/verify', methods=['GET'])
    def get_user():
        request = app.current_request
        auth_token = request.headers['authorization']
        refresh_token = request.headers['refresh']

        try:
            response = auth_service.verify_user(auth_token, refresh_token)
            return Response(body=response, status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
