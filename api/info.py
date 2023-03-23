import fastapi

from fastapi import Request

from main import limiter, RATE_LIMITS

router = fastapi.APIRouter()

@router.get('/', tags=['Info'])
@limiter.limit('3/second')
def root(request: Request):
    """Redirect to docs. This won't work when the "Try it out" button in the documentation is pressed, as it returns a redirect, not an usual response."""
    return fastapi.responses.RedirectResponse(url='/docs')

@router.get('/uptime', tags=['Info'])
def root(request: Request):
    """Redirects to the uptime overview. This won't work when the "Try it out" button in the documentation is pressed, as it returns a redirect, not an usual response."""
    return fastapi.responses.RedirectResponse(url='https://github.com/nsde/uptime#readme')

@router.get('/status', tags=['Info'])
def status(request: Request):
    """Returns the status of the API. Used for health checks."""
    return {'status': 'ok'}

@router.get('/rate-limits', tags=['Info'])
def rate_limits(request: Request) -> list:
    """Returns the rate limits for the API."""
    return RATE_LIMITS
