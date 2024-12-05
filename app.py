from chalice import Chalice, CORSConfig, Response
from chalicelib.routes.auth_routes import auth_route
from chalicelib.routes.profile_routes import profile_routes
from chalicelib.routes.subscription_routes import create_subscription_routes as subscription_routes
from chalicelib.routes.payment_routes import create_payment_routes as payment_routes
from chalicelib.routes.user_purchase_routes import create_user_purchase_routes as user_purchase_routes
app = Chalice(app_name='analisa')


app.register_blueprint(profile_routes)
app.register_blueprint(auth_route)

# auth_routes(app)
# profile_routes(app)
subscription_routes(app)
payment_routes(app)
user_purchase_routes(app)


@app.route('/')
def index():
    return {'hello': 'world'}
