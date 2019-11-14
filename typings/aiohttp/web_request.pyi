"""
This type stub file was generated by pyright.
"""

import asyncio
import datetime
import re
import string
import attr
from typing import Any, Dict, Iterator, Mapping, MutableMapping, Optional, TYPE_CHECKING, Tuple, Union
from multidict import CIMultiDictProxy, MultiDictProxy
from yarl import URL
from .abc import AbstractStreamWriter
from .helpers import ChainMapProxy, DEBUG, HeadersMixin, reify
from .http_parser import RawRequestMessage
from .multipart import MultipartReader
from .streams import StreamReader
from .typedefs import JSONDecoder, LooseHeaders, RawHeaders, StrOrURL
from .web_response import StreamResponse
from .web_app import Application
from .web_urldispatcher import UrlMappingMatchInfo
from .web_protocol import RequestHandler

__all__ = ('BaseRequest', 'FileField', 'Request')
if TYPE_CHECKING:
    ...
@attr.s(frozen=True, slots=True)
class FileField:
    name = ...
    filename = ...
    file = ...
    content_type = ...
    headers = ...


_TCHAR = string.digits + string.ascii_letters + r"!#$%&'*+.^_`|~-"
_TOKEN = r'[{tchar}]+'.format(tchar=_TCHAR)
_QDTEXT = r'[{}]'.format(r''.join(chr(c) for c in (9, 32, 33) + tuple(range(35, 127))))
_QUOTED_PAIR = r'\\[\t !-~]'
_QUOTED_STRING = r'"(?:{quoted_pair}|{qdtext})*"'.format(qdtext=_QDTEXT, quoted_pair=_QUOTED_PAIR)
_FORWARDED_PAIR = r'({token})=({token}|{quoted_string})(:\d{{1,4}})?'.format(token=_TOKEN, quoted_string=_QUOTED_STRING)
_QUOTED_PAIR_REPLACE_RE = re.compile(r'\\([\t !-~])')
_FORWARDED_PAIR_RE = re.compile(_FORWARDED_PAIR)
class BaseRequest(MutableMapping[str, Any], HeadersMixin):
    POST_METHODS = ...
    ATTRS = ...
    def __init__(self, message: RawRequestMessage, payload: StreamReader, protocol: RequestHandler, payload_writer: AbstractStreamWriter, task: asyncio.Task[None], loop: asyncio.AbstractEventLoop, *, client_max_size: int = ..., state: Optional[Dict[str, Any]] = ..., scheme: Optional[str] = ..., host: Optional[str] = ..., remote: Optional[str] = ...) -> None:
        ...
    
    def clone(self, *, method: str = ..., rel_url: StrOrURL = ..., headers: LooseHeaders = ..., scheme: str = ..., host: str = ..., remote: str = ...) -> BaseRequest:
        """Clone itself with replacement some attributes.

        Creates and returns a new instance of Request object. If no parameters
        are given, an exact copy is returned. If a parameter is not passed, it
        will reuse the one from the current request object.

        """
        ...
    
    @property
    def task(self) -> asyncio.Task[None]:
        ...
    
    @property
    def protocol(self) -> RequestHandler:
        ...
    
    @property
    def transport(self) -> Optional[asyncio.Transport]:
        ...
    
    @property
    def writer(self) -> AbstractStreamWriter:
        ...
    
    @reify
    def message(self) -> RawRequestMessage:
        ...
    
    @reify
    def rel_url(self) -> URL:
        ...
    
    @reify
    def loop(self) -> asyncio.AbstractEventLoop:
        ...
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def __setitem__(self, key: str, value: Any) -> None:
        ...
    
    def __delitem__(self, key: str) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    @reify
    def secure(self) -> bool:
        """A bool indicating if the request is handled with SSL."""
        ...
    
    @reify
    def forwarded(self) -> Tuple[Mapping[str, str], ...]:
        """A tuple containing all parsed Forwarded header(s).

        Makes an effort to parse Forwarded headers as specified by RFC 7239:

        - It adds one (immutable) dictionary per Forwarded 'field-value', ie
          per proxy. The element corresponds to the data in the Forwarded
          field-value added by the first proxy encountered by the client. Each
          subsequent item corresponds to those added by later proxies.
        - It checks that every value has valid syntax in general as specified
          in section 4: either a 'token' or a 'quoted-string'.
        - It un-escapes found escape sequences.
        - It does NOT validate 'by' and 'for' contents as specified in section
          6.
        - It does NOT validate 'host' contents (Host ABNF).
        - It does NOT validate 'proto' contents for valid URI scheme names.

        Returns a tuple containing one or more immutable dicts
        """
        ...
    
    @reify
    def scheme(self) -> str:
        """A string representing the scheme of the request.

        Hostname is resolved in this order:

        - overridden value by .clone(scheme=new_scheme) call.
        - type of connection to peer: HTTPS if socket is SSL, HTTP otherwise.

        'http' or 'https'.
        """
        ...
    
    @reify
    def method(self) -> str:
        """Read only property for getting HTTP method.

        The value is upper-cased str like 'GET', 'POST', 'PUT' etc.
        """
        ...
    
    @reify
    def version(self) -> Tuple[int, int]:
        """Read only property for getting HTTP version of request.

        Returns aiohttp.protocol.HttpVersion instance.
        """
        ...
    
    @reify
    def host(self) -> str:
        """Hostname of the request.

        Hostname is resolved in this order:

        - overridden value by .clone(host=new_host) call.
        - HOST HTTP header
        - socket.getfqdn() value
        """
        ...
    
    @reify
    def remote(self) -> Optional[str]:
        """Remote IP of client initiated HTTP request.

        The IP is resolved in this order:

        - overridden value by .clone(remote=new_remote) call.
        - peername of opened socket
        """
        ...
    
    @reify
    def url(self) -> URL:
        ...
    
    @reify
    def path(self) -> str:
        """The URL including *PATH INFO* without the host or scheme.

        E.g., ``/app/blog``
        """
        ...
    
    @reify
    def path_qs(self) -> str:
        """The URL including PATH_INFO and the query string.

        E.g, /app/blog?id=10
        """
        ...
    
    @reify
    def raw_path(self) -> str:
        """ The URL including raw *PATH INFO* without the host or scheme.
        Warning, the path is unquoted and may contains non valid URL characters

        E.g., ``/my%2Fpath%7Cwith%21some%25strange%24characters``
        """
        ...
    
    @reify
    def query(self) -> MultiDictProxy[str]:
        """A multidict with all the variables in the query string."""
        ...
    
    @reify
    def query_string(self) -> str:
        """The query string in the URL.

        E.g., id=10
        """
        ...
    
    @reify
    def headers(self) -> CIMultiDictProxy[str]:
        """A case-insensitive multidict proxy with all headers."""
        ...
    
    @reify
    def raw_headers(self) -> RawHeaders:
        """A sequence of pairs for all headers."""
        ...
    
    @staticmethod
    def _http_date(_date_str: str) -> Optional[datetime.datetime]:
        """Process a date string, return a datetime object
        """
        ...
    
    @reify
    def if_modified_since(self) -> Optional[datetime.datetime]:
        """The value of If-Modified-Since HTTP header, or None.

        This header is represented as a `datetime` object.
        """
        ...
    
    @reify
    def if_unmodified_since(self) -> Optional[datetime.datetime]:
        """The value of If-Unmodified-Since HTTP header, or None.

        This header is represented as a `datetime` object.
        """
        ...
    
    @reify
    def if_range(self) -> Optional[datetime.datetime]:
        """The value of If-Range HTTP header, or None.

        This header is represented as a `datetime` object.
        """
        ...
    
    @reify
    def keep_alive(self) -> bool:
        """Is keepalive enabled by client?"""
        ...
    
    @reify
    def cookies(self) -> Mapping[str, str]:
        """Return request cookies.

        A read-only dictionary-like object.
        """
        ...
    
    @reify
    def http_range(self) -> slice:
        """The content of Range HTTP header.

        Return a slice instance.

        """
        ...
    
    @reify
    def content(self) -> StreamReader:
        """Return raw payload stream."""
        ...
    
    @property
    def has_body(self) -> bool:
        """Return True if request's HTTP BODY can be read, False otherwise."""
        ...
    
    @property
    def can_read_body(self) -> bool:
        """Return True if request's HTTP BODY can be read, False otherwise."""
        ...
    
    @reify
    def body_exists(self) -> bool:
        """Return True if request has HTTP BODY, False otherwise."""
        ...
    
    async def release(self) -> None:
        """Release request.

        Eat unread part of HTTP BODY if present.
        """
        ...
    
    async def read(self) -> bytes:
        """Read request body if present.

        Returns bytes object with full request content.
        """
        ...
    
    async def text(self) -> str:
        """Return BODY as text using encoding from .charset."""
        ...
    
    async def json(self, *, loads: JSONDecoder = ...) -> Any:
        """Return BODY as JSON."""
        ...
    
    async def multipart(self) -> MultipartReader:
        """Return async iterator to process BODY as multipart."""
        ...
    
    async def post(self) -> MultiDictProxy[Union[str, bytes, FileField]]:
        """Return POST parameters."""
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other: object) -> bool:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    async def _prepare_hook(self, response: StreamResponse) -> None:
        ...
    


class Request(BaseRequest):
    ATTRS = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    
    if DEBUG:
        def __setattr__(self, name: str, val: Any) -> None:
            ...
        
    def clone(self, *, method: str = ..., rel_url: StrOrURL = ..., headers: LooseHeaders = ..., scheme: str = ..., host: str = ..., remote: str = ...) -> Request:
        ...
    
    @reify
    def match_info(self) -> UrlMappingMatchInfo:
        """Result of route resolving."""
        ...
    
    @property
    def app(self) -> Application:
        """Application instance."""
        ...
    
    @property
    def config_dict(self) -> ChainMapProxy:
        ...
    
    async def _prepare_hook(self, response: StreamResponse) -> None:
        ...
    


