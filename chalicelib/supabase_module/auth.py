from chalicelib.supabase_module.supabase_config import supabase


def supabase_signup(data: dict) -> object:
    return supabase.auth.sign_up(data)


def supabase_login(data: dict) -> dict:
    response = supabase.auth.sign_in_with_password(data)
    return {
        'access_token': response.session.access_token,
        'refresh_token': response.session.refresh_token,
    }


def supabase_logout(auth_token: str) -> dict:
    supabase.auth.sign_out()
    return {'message': 'Logged out'}


def supabase_get_user(auth_token: str) -> dict:
    return supabase.auth.get_user(auth_token).user


def supabase_generate_session() -> dict:
    return supabase.auth.refresh_session()
