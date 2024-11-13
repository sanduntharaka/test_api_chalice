from services.subscription_service import SubscriptionService


def create_subscription_routes(app):
    subscription_service = SubscriptionService()

    @app.route('/subscription-plans', methods=['GET'])
    def get_all_loyalty_programs():
        return subscription_service.get_all_subscription_plans()

    @app.route('/subscription-plans/{id}', methods=['GET'])
    def get_loyalty_program_by_id(id):
        return subscription_service.get_subscription_plan_by_id(id)

    @app.route('/subscription-cards', methods=['POST'])
    def subscribe_to_loyalty_program():
        request = app.current_request
        auth_token = request.headers['authorization']
        request_data = {
            "program_id": request.json_body['program_id'],
            "date": request.json_body['datetime']
        }
        return subscription_service.subscribe_to_subscription_plan(auth_token, request_data)

    @app.route('/subscription-cards', methods=['GET'])
    def get_user_loyalty_cards():
        request = app.current_request
        auth_token = request.headers['authorization']
        return subscription_service.get_all_user_subscription_cards(auth_token)

    @app.route('/subscription-cards/{id}', methods=['GET'])
    def get_user_loyalty_card_by_id(id):
        request = app.current_request
        auth_token = request.headers['authorization']
        return subscription_service.get_user_subscription_card_by_id(auth_token, id)

    @app.route('/subscription-cards/{id}', methods=['PUT'])
    def get_user_loyalty_card_by_id(id):
        request = app.current_request
        auth_token = request.headers['authorization']
        request_data = {
            "status": request.json_body['status']
        }
        return subscription_service.update_user_subscription_card(auth_token, id, request_data)
