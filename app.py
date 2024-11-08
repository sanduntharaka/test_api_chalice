from chalice import Chalice
from routes.auth_routes import create_auth_routes as auth_routes
from routes.profile_routes import create_profile_routes as profile_routes

app = Chalice(app_name='analisa')


auth_routes(app)
profile_routes(app)


@app.route('/')
def index():
    return {'hello': 'world'}
