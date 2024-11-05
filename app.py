from chalice import Chalice
from supabase_module.auth import supabase_login, supabase_logout
app = Chalice(app_name='analisa')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/login', methods=['POST'])
def login():
    request = app.current_request
    response = supabase_login(
        {
            'email': request.json_body['email'],
            'password': request.json_body['password']
        }
    )
    return response


# @app.route('/logout', methods=['get'])
# def login():

#     response = supabase_logout()
#     return response
