from chalice import Chalice, CORSConfig, Response
from chalicelib.routes.auth_routes import create_auth_routes as auth_routes
from chalicelib.routes.profile_routes import create_profile_routes as profile_routes
from chalicelib.routes.subscription_routes import create_subscription_routes as subscription_routes
from chalicelib.routes.payment_routes import create_payment_routes as payment_routes
from chalicelib.routes.user_purchase_routes import create_user_purchase_routes as user_purchase_routes
app = Chalice(app_name='analisa')

# Shared CORS configuration
cors_config = CORSConfig(
    allow_origin='http://localhost:8100',  # Replace with your front-end URL
    # Include necessary headers
    allow_headers=['Content-Type'],
    max_age=600,  # Cache preflight response for 10 minutes
    # Optional: Expose custom headers if needed
    expose_headers=['X-Custom-Header'],
)

# CORS_HEADERS = {
#     'Access-Control-Allow-Origin': 'http://localhost:8100',  # Your frontend origin
#     'Access-Control-Allow-Headers': 'Content-Type, Authorization',
#     'Access-Control-Allow-Methods': 'OPTIONS, POST',
# }

# # Import and register route handlers


# def auth_routes(app):
#     @app.route('/test',  methods=['POST'], cors=True)
#     def test():
#         return {'message': 'Auth route'}


# def profile_routes(app):
#     @app.route('/profile', methods=['GET'], cors=cors_config)
#     def profile():
#         return {'message': 'Profile route'}


# def subscription_routes(app):
#     @app.route('/subscription', methods=['GET', 'POST'], cors=cors_config)
#     def subscription():
#         return {'message': 'Subscription route'}


# def payment_routes(app):
#     @app.route('/payment', methods=['POST'], cors=cors_config)
#     def payment():
#         return {'message': 'Payment route'}


# def user_purchase_routes(app):
#     @app.route('/purchase', methods=['GET', 'POST'], cors=cors_config)
#     def purchase():
#         return {'message': 'Purchase route'}


# @app.middleware('http')
# def add_cors_headers(event, get_response):
#     response = get_response(event)
#     if isinstance(response, Response):
#         response.headers.update(cors_config)
#     return response


auth_routes(app)
profile_routes(app)
subscription_routes(app)
payment_routes(app)
user_purchase_routes(app)


@app.route('/')
def index():
    return {'hello': 'world'}
