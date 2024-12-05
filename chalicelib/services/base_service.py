from chalicelib.services.auth_service import AuthService
from chalice import Response


class BaseService:
    def __init__(self):
        self.auth_service = AuthService()

    def get_user_details(self, token):

        try:
            user = self.auth_service.get_user(token)
            return user
        except Exception as e:
            raise Exception(f"Error fetching user details: {str(e)}")
