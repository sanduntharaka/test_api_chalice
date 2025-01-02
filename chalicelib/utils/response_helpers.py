from chalice import (
    Response,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    ConflictError,
    UnprocessableEntityError,
    TooManyRequestsError,
    ChaliceViewError
)


def create_response(body: dict, status_code: int = 200) -> Response:

    headers = {'Content-Type': 'application/json'}
    # error_map = {
    #     400: BadRequestError,
    #     401: UnauthorizedError,
    #     403: ForbiddenError,
    #     404: NotFoundError,
    #     409: ConflictError,
    #     422: UnprocessableEntityError,
    #     429: TooManyRequestsError
    # }

    # if status_code in [200, 201]:
    #     return Response(body=body, status_code=status_code, headers=headers)
    # elif status_code in error_map:
    #     raise error_map[status_code](body.get('error', 'An error occurred.'))
    # else:
    #     raise ChaliceViewError(body.get('error', 'An unknown error occurred.'))
    return Response(body=body, status_code=status_code, headers=headers)
