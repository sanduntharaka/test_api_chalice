from supabase_module.db_query import insert, call_function
from services.auth_service import AuthService
from supabase_module.setup_session import setup_session


class UserPurchaseService:
    auth_service = AuthService()

    def create_user_purchase(self, token, purchase_data):

        user = self.auth_service.get_user(token)
    # add loop
        data = {
            "order": {
                "odoo_order_id": 2,
                "amount": 1,
                "user_id": user.id
            },
            "order_products": [{
                "odoo_product_id": 1,
                "product_name": "abcd",
                "product_description": "adasd jadad",
                "product_price": 10,
                "qty": 1,
                "free_qty": 0,
                "user_id": user.id

            }]
        }
        return call_function('add_order_data',  {"order_data": data})
