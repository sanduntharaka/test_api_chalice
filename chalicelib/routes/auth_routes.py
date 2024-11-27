from chalicelib.services.auth_service import AuthService
from chalice import Response


def create_auth_routes(app):
    auth_service = AuthService()

    @app.route('/sign-up', methods=['POST'])
    def sign_up():
        request = app.current_request
        email = request.json_body['email']
        password = request.json_body['password']
        try:
            return Response(body=auth_service.sign_up(email, password), status_code=200)
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
            return Response(body=auth_service.logout(auth_token,refresh_token), status_code=200)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
