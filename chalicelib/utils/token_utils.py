from chalice import BadRequestError
from chalicelib.models.auth_models import AuthTokens


def extract_tokens(headers: dict) -> AuthTokens:
    try:
        return AuthTokens(
            auth_token=headers.get('authorization'),
            refresh_token=headers.get('refresh')
        )
    except KeyError:
        raise BadRequestError("Missing required tokens.")
