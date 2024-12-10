from chalicelib.services.auth_service import AuthService
from chalice import (
    UnauthorizedError,
)


class BaseService:
    def __init__(self):
        self.auth_service = AuthService()

    def get_user_details(self, token):
        user = self.auth_service.get_user(token)
        return user
