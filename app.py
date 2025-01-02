from chalice import Chalice, CORSConfig, Response
from chalicelib.routes.auth_routes import auth_route
from chalicelib.routes.profile_routes import profile_routes
from chalicelib.routes.subscription_routes import subscription_routes
from chalicelib.routes.payment_routes import payment_routes
from chalicelib.routes.user_purchase_routes import purchase_routes
app = Chalice(app_name='analisa')


app.register_blueprint(auth_route)
app.register_blueprint(profile_routes)
app.register_blueprint(subscription_routes)
app.register_blueprint(payment_routes)
app.register_blueprint(purchase_routes)

# auth_routes(app)
# profile_routes(app)
# subscription_routes(app)
# payment_routes(app)
# user_purchase_routes(app)


@app.route('/')
def index():
    return {'hello': 'world'}
