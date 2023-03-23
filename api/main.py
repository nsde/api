import fastapi
import slowapi
import importlib

from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

RATE_LIMITS = ['5000/hour', '100/minute', '10/second']

app = fastapi.FastAPI()
limiter = slowapi.Limiter(key_func=get_remote_address, default_limits=RATE_LIMITS, enabled=True)
app.state.limiter = limiter
app.add_exception_handler(slowapi.errors.RateLimitExceeded, slowapi._rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

for module in ['gpt', 'info', 'music', 'other']:
    router = importlib.import_module(module).router
    app.include_router(router)
