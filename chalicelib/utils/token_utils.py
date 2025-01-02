from chalicelib.models.auth_models import AuthTokens
from chalicelib.decorators.handle_exceptions import handle_exceptions


def extract_tokens(headers: dict) -> AuthTokens:
    return AuthTokens(
        access_token=headers.get('authorization'),
        refresh_token=headers.get('refresh')
    )
