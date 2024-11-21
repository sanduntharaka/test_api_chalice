from chalicelib.services.profile_service import ProfileService


def create_profile_routes(app):
    profile_service = ProfileService()

    @app.route('/profile', methods=['POST'])
    def create_user_profile():
        request = app.current_request
        auth_token = request.headers['authorization']
        profile_data = {
            'first_name': request.json_body['first_name'],
            'last_name': request.json_body['last_name'],
            'phone': request.json_body['phone'],
            'dob': request.json_body['dob'],
        }
        return profile_service.create_profile(auth_token, profile_data)

    @app.route('/profile/me', methods=['GET'])
    def get_user_profile():
        request = app.current_request
        auth_token = request.headers['authorization']
        return profile_service.get_profile(auth_token)

    @app.route('/profile/me', methods=['PUT'])
    def update_user_profile():
        request = app.current_request
        auth_token = request.headers['authorization']
        refresh_token = request.headers['refresh']
        profile_data = {
            'first_name': request.json_body['first_name'],
            'last_name': request.json_body['last_name'],
            'phone': request.json_body['phone'],
            'dob': request.json_body['dob'],
        }
        return profile_service.update_profile(auth_token, refresh_token, profile_data)

    @app.route('/profiles', methods=['GET'])
    def get_all_user_profiles():
        return profile_service.get_all_profiles()
