"""Import all routers and add them to routers_list."""
from .user import user_router
from .social import social_router

routers_list = [
    user_router,
    social_router,
]

__all__ = [
    "routers_list",
]