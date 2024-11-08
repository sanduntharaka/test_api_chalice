from services.auth_service import AuthService


def create_auth_routes(app):
    auth_service = AuthService()

    @app.route('/login', methods=['POST'])
    def login():
        request = app.current_request
        email = request.json_body['email']
        password = request.json_body['password']
        return auth_service.login(email, password)

    @app.route('/logout', methods=['POST'])
    def logout():
        request = app.current_request
        auth_token = request.headers['authorization']
        return auth_service.logout(auth_token)
