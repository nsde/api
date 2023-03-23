import os
import httpx
import fastapi

from fastapi import Request
from dotenv import load_dotenv

from main import limiter

load_dotenv()
router = fastapi.APIRouter()

@router.get('/spotify/lyrics', response_class=fastapi.responses.PlainTextResponse, tags=['Music'])
@limiter.limit('5/second')
def get_lyrics_from_spotify(request: Request, track: str) -> str:
    """Returns the lyrics of a Spotify track by its ID or URL in plain text. If the lyrics are not available, it will return an empty string."""

    track_url = track
    if not '://' in track:
        track_url = 'https://open.spotify.com/track/' + track

    resp = httpx.get(
        url=f'https://{os.getenv("SPOTIFY_LYRICS_DOMAIN")}',
        params={'url': track_url},
        timeout=3
    ).json()

    try:
        text = '\n'.join([line['words'] for line in resp['lines'] if line['words'] and line['words'] != '♪'])
    except KeyError:
        text = ''
    return text
