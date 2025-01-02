from chalice import CORSConfig
cors_config = CORSConfig(
    allow_origin='*',
    # allow_headers=['X-Special-Header'],
    # max_age=600,
    # expose_headers=['X-Special-Header'],
    # allow_credentials=True
)
