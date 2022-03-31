from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication


@database_sync_to_async
def get_user(raw_token):
    auth = JWTAuthentication()
    validated_token = auth.get_validated_token(raw_token)
    return auth.get_user(validated_token)


class JWTTokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        scope = dict(scope)
        try:
            raw_token = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
        except ValueError:
            raw_token = None
        if 'user' not in scope:
            scope['user'] = await get_user(raw_token)

        return await super().__call__(scope, receive, send)
