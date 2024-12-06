from chalicelib.services.payment_service import PaymentService
from chalicelib.utils.token_utils import extract_tokens

from chalice import Blueprint

payment_routes = Blueprint(__name__)
payment_service = PaymentService()


@payment_routes.route('/payment', methods=['GET'])
def get_all_user_payments():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)
    return payment_service.get_all_payments(tokens.access_token)


@payment_routes.route('/payment/filter', methods=['GET'])
def filter_payments_by_date_range():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)

    start_date = payment_routes.current_request.query_params.get('start_date')
    end_date = payment_routes.current_request.query_params.get('end_date')
    return payment_service.filter_payments_by_date_range(tokens.access_token, tokens.refresh_token, start_date, end_date)


@payment_routes.route('/payment', methods=['POST'])
def add_payment():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)

    request_data = {
        "amount": request.json_body['amount'],
        "date_time": request.json_body['date_time'],
        "type": request.json_body['type'],
        "program_id": request.json_body['program_id']
    }
    return payment_service.add_payment(tokens.access_token, request_data)


@payment_routes.route('/web-hook/card', methods=['POST'])
def test_payment():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)
    order_amount = request.json_body['amount']
    return payment_service.reduce_card_amount(tokens.access_token, order_amount)
