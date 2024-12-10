from chalicelib.services.user_purchase_service import UserPurchaseService
from chalicelib.utils.token_utils import extract_tokens
from chalicelib.utils.response_helpers import create_response
from chalicelib.decorators.handle_exceptions import handle_exceptions
from chalicelib.models.purchase_model import OrderRequest
from chalice import Blueprint


purchase_routes = Blueprint(__name__)
purchase_service = UserPurchaseService()


@purchase_routes.route('/user-purchase', methods=['POST'])
@handle_exceptions
def create_user_purchase():
    request = purchase_routes.current_request

    tokens = extract_tokens(request.headers)
    body = OrderRequest.parse_obj(request.json_body)

    return purchase_service.create_user_purchase(tokens.access_token, body)
