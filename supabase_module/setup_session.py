from .supabase_config import supabase


def setup_session(access_token, refresh_token):
    supabase.auth.set_session(access_token, refresh_token)
