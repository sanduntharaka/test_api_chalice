from chalicelib.supabase_module.supabase_config import supabase


def supabase_signup(data) -> dict:
    try:
        response = supabase.auth.sign_up(data)
        return {
            'access_token': response.session.access_token if response.session.access_token else None,
            'refresh_token': response.session.refresh_token if response.session.refresh_token else None,
        }
    except Exception as e:
        print(e)
        return {'error': str(e), 'message': 'Error signing up'}


def supabase_login(data) -> dict:
    response = supabase.auth.sign_in_with_password(data)
    return {
        'access_token': response.session.access_token,
        'refresh_token': response.session.refresh_token,
    }


def supabase_logout(JWT) -> dict:
    try:
        supabase.auth.sign_out()
        return {'message': 'Logged out'}
    except Exception as e:
        return {'error': str(e), 'message': 'Error logging out'}


def supabase_get_user(jwt) -> dict:
    response = supabase.auth.get_user(jwt)
    return response.user
