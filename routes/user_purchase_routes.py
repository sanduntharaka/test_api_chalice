from services.user_purchase_service import UserPurchaseService


def create_user_purchase_routes(app):
    purchase_service = UserPurchaseService()

    @app.route('/user-purchase', methods=['POST'])
    def create_user_purchase():
        request = app.current_request
        auth_token = request.headers['authorization']
        return purchase_service.create_user_purchase(auth_token, request.json_body)
