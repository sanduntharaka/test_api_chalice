from chalicelib.services.payment_service import PaymentService
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.models.payment_model import AddPaymentModel, CardReducePaymentWebHook
from chalicelib.utils.response_helpers import create_response
from chalicelib.decorators.handle_exceptions import handle_exceptions
from chalicelib.config import cors_config

from chalice import Blueprint

payment_routes = Blueprint(__name__)
payment_service = PaymentService()


@payment_routes.route('/payment', methods=['GET'], cors=cors_config)
@handle_exceptions
def get_all_user_payments():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)
    response = payment_service.get_all_payments(tokens.access_token)
    return create_response(response, status_code=200)


@payment_routes.route('/payment/filter', methods=['GET'], cors=cors_config)
@handle_exceptions
def filter_payments_by_date_range():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)

    start_date = payment_routes.current_request.query_params.get(
        'start_date')
    end_date = payment_routes.current_request.query_params.get('end_date')
    response = payment_service.filter_payments_by_date_range(
        tokens.access_token, start_date, end_date)
    return create_response(response, status_code=200)


@payment_routes.route('/payment', methods=['POST'], cors=cors_config)
@handle_exceptions
def add_payment():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)

    request_data = AddPaymentModel.model_validate(
        {
            "amount": request.json_body['amount'],
            "date_time": request.json_body['date_time'],
            "type": request.json_body['type'],
            "program_id": request.json_body['program_id']
        }

    )
    response = payment_service.add_payment(
        tokens.access_token, request_data)
    return create_response(response, status_code=201)


@payment_routes.route('/web-hook/card', methods=['POST'], cors=cors_config)
@handle_exceptions
def reduce_card_amount():
    request = payment_routes.current_request
    tokens = extract_tokens(request.headers)
    body = CardReducePaymentWebHook.parse_obj(request.json_body)
    response = payment_service.reduce_card_amount(
        tokens.access_token, body)
    return create_response(response, status_code=200)
