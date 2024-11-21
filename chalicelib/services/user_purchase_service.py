from chalicelib.supabase_module.db_query import insert, call_function
from chalicelib.services.auth_service import AuthService
from chalicelib.supabase_module.setup_session import setup_session
from chalice import Response


class UserPurchaseService:
    auth_service = AuthService()

    def create_user_purchase(self, token, purchase_data):
        try:
            user = self.auth_service.get_user(token)
        except Exception as e:
            return Response(body={'error': str(e)}, status_code=400)
        data = {
            "order": {
                "odoo_order_id": purchase_data['order']['odoo_order_id'],
                "amount": purchase_data['order']['order_amount'],
                "user_id": user.id
            },
            "order_products": [{
                "odoo_product_id": i['odoo_product_id'],
                "product_name":  i['product_name'],
                "product_description": i['product_description'],
                "product_price":  i['product_price'],
                "qty":  i['qty'],
                "free_qty":  i['free_qty'],
                "user_id": user.id

            } for i in purchase_data['order_products']]
        }
        return call_function('add_order_data',  {"order_data": data})
