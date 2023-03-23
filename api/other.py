import httpx
import fastapi

from typing import Union
from fastapi import Request
from dotenv import load_dotenv

load_dotenv()
router = fastapi.APIRouter()

# @router.get('/book', response_class=fastapi.responses.PlainTextResponse, tags=['Other'])
# def get_book_info_by_isbn(request: Request, isbn: Union[str, int]):
#     """Returns info of a book by its ISBN."""
#     # get json data from https://openlibrary.org/api/volumes/brief/isbn/{isbn}.json'

#     resp = httpx.get(f'https://openlibrary.org/api/volumes/brief/isbn/{isbn}.json', timeout=3).content.decode('utf-8')
#     # to dict:
#     import json
#     test_json = """{"records": {"/books/OL35691100M": {"isbns": ["3200076364", "9783200076365"], "issns": [], "lccns": [], "oclcs": [], "olids": ["OL35691100M"], "publishDates": [""], "recordURL": "https://openlibrary.org/books/OL35691100M/Der_Pakt", "data": {"url": "https://openlibrary.org/books/OL35691100M/Der_Pakt", "key": "/books/OL35691100M", "title": "Der Pakt", "identifiers": {"isbn_10": ["3200076364"], "isbn_13": ["9783200076365"], "openlibrary": ["OL35691100M"]}, "cover": {"small": "https://covers.openlibrary.org/b/id/12390103-S.jpg", "medium": "https://covers.openlibrary.org/b/id/12390103-M.jpg", "large": "https://covers.openlibrary.org/b/id/12390103-L.jpg"}}, "details": {"bib_key": "isbn:3200076364", "info_url": "https://openlibrary.org/books/OL35691100M/Der_Pakt", "preview": "noview", "preview_url": "https://openlibrary.org/books/OL35691100M/Der_Pakt", "thumbnail_url": "https://covers.openlibrary.org/b/id/12390103-S.jpg", "details": {"type": {"key": "/type/edition"}, "title": "Der Pakt", "source_records": ["amazon:3200076364"], "isbn_10": ["3200076364"], "isbn_13": ["9783200076365"], "physical_format": "hardcover", "full_title": "Der Pakt", "covers": [12390103], "works": [{"key": "/works/OL26425526W"}], "key": "/books/OL35691100M", "latest_revision": 1, "revision": 1, "created": {"type": "/type/datetime", "value": "2021-12-01T22:58:51.863249"}, "last_modified": {"type": "/type/datetime", "value": "2021-12-01T22:58:51.863249"}}}}}, "items": []}"""
#     resp = json.loads(test_json)

#     return resp
