from pydantic import ValidationError
from functools import wraps
from chalicelib.utils.response_helpers import create_response
from chalice import (
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    ConflictError,
    UnprocessableEntityError,
    TooManyRequestsError,
    ChaliceViewError
)
from supabase.client import AuthApiError


def handle_exceptions(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):

        try:
            return handler(*args, **kwargs)
        except ValidationError as ve:
            return create_response({'message': 'bad request. check your data', 'error': str(ve)}, status_code=400)
        except UnauthorizedError as ue:
            return create_response({'message': 'token expire or invalid', 'error': str(ue)}, status_code=401)
        except AuthApiError as ae:
            return create_response({'message': 'authentication error', 'error': str(ae)}, status_code=401)

        except Exception as e:
            return create_response({'message': 'Internal server error', 'error': str(e)}, status_code=500)
    return wrapper
