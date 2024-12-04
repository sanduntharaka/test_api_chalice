from chalice import Response


def create_response(body: dict, status_code: int = 200) -> Response:
    return Response(body=body, status_code=status_code, headers={'Content-Type': 'application/json'})
