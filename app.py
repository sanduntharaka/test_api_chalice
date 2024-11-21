from chalice import Chalice
from chalicelib.routes.auth_routes import create_auth_routes as auth_routes
from chalicelib.routes.profile_routes import create_profile_routes as profile_routes
from chalicelib.routes.subscription_routes import create_subscription_routes as subscription_routes
from chalicelib.routes.payment_routes import create_payment_routes as payment_routes
from chalicelib.routes.user_purchase_routes import create_user_purchase_routes as user_purchase_routes
app = Chalice(app_name='analisa')


auth_routes(app)
profile_routes(app)
subscription_routes(app)
payment_routes(app)
user_purchase_routes(app)


@app.route('/')
def index():
    return {'hello': 'world'}
