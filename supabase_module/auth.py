from .supbase_config import supabase


def supabase_login(data) -> dict:
    response = supabase.auth.sign_in_with_password(data)
    return {
        'access_token': response.session.access_token,
        'refresh_token': response.session.refresh_token,
    }


def supabase_logout() -> dict:
    response = supabase.auth.sign_out()
    return response


def supabase_get_user(jwt) -> dict:
    response = supabase.auth.get_user(jwt)
    return response.user
