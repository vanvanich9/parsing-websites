from . import (
    general,
    authorization,
    parsing,
)

routers = (
	general.router,
    authorization.router,
    parsing.router,
)