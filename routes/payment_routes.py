from services.payment_service import PaymentService


def create_payment_routes(app):
    payment_service = PaymentService()

    @app.route('/payment', methods=['GET'])
    def get_all_user_payments():
        request = app.current_request
        auth_token = request.headers['authorization']
        return payment_service.get_all_payments(auth_token)

    @app.route('/payment/filter', methods=['GET'])
    def filter_payments_by_date_range():
        request = app.current_request
        auth_token = request.headers['authorization']
        start_date = app.current_request.query_params.get('start_date')
        end_date = app.current_request.query_params.get('end_date')
        return payment_service.filter_payments_by_date_range(auth_token, start_date, end_date)

    @app.route('/payment', methods=['POST'])
    def add_payment():
        request = app.current_request
        auth_token = request.headers['authorization']
        request_data = {
            "amount": request.json_body['amount'],
            "date_time": request.json_body['date_time'],
            "type": request.json_body['type'],
            "program_id": request.json_body['program_id']
        }
        return payment_service.add_payment(auth_token, request_data)
