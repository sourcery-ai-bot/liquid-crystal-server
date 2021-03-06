"""
This type stub file was generated by pyright.
"""

import asyncio
import collections
import re
import sys
from enum import IntEnum
from struct import Struct
from typing import Any, Callable, List, Optional, Tuple, Union
from .base_protocol import BaseProtocol
from .helpers import NO_EXTENSIONS
from .streams import DataQueue

"""WebSocket protocol versions 13 and 8."""
__all__ = ('WS_CLOSED_MESSAGE', 'WS_CLOSING_MESSAGE', 'WS_KEY', 'WebSocketReader', 'WebSocketWriter', 'WSMessage', 'WebSocketError', 'WSMsgType', 'WSCloseCode')
class WSCloseCode(IntEnum):
    OK = ...
    GOING_AWAY = ...
    PROTOCOL_ERROR = ...
    UNSUPPORTED_DATA = ...
    INVALID_TEXT = ...
    POLICY_VIOLATION = ...
    MESSAGE_TOO_BIG = ...
    MANDATORY_EXTENSION = ...
    INTERNAL_ERROR = ...
    SERVICE_RESTART = ...
    TRY_AGAIN_LATER = ...


ALLOWED_CLOSE_CODES = int(i) for i in WSCloseCode
class WSMsgType(IntEnum):
    CONTINUATION = ...
    TEXT = ...
    BINARY = ...
    PING = ...
    PONG = ...
    CLOSE = ...
    CLOSING = ...
    CLOSED = ...
    ERROR = ...
    text = ...
    binary = ...
    ping = ...
    pong = ...
    close = ...
    closing = ...
    closed = ...
    error = ...


WS_KEY = b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
UNPACK_LEN2 = Struct('!H').unpack_from
UNPACK_LEN3 = Struct('!Q').unpack_from
UNPACK_CLOSE_CODE = Struct('!H').unpack
PACK_LEN1 = Struct('!BB').pack
PACK_LEN2 = Struct('!BBH').pack
PACK_LEN3 = Struct('!BBQ').pack
PACK_CLOSE_CODE = Struct('!H').pack
MSG_SIZE = 2 ** 14
DEFAULT_LIMIT = 2 ** 16
_WSMessageBase = collections.namedtuple('_WSMessageBase', ['type', 'data', 'extra'])
class WSMessage(_WSMessageBase):
    def json(self, *, loads: Callable[[Any], Any] = ...) -> Any:
        """Return parsed JSON data.

        .. versionadded:: 0.22
        """
        ...
    


WS_CLOSED_MESSAGE = WSMessage(WSMsgType.CLOSED, None, None)
WS_CLOSING_MESSAGE = WSMessage(WSMsgType.CLOSING, None, None)
class WebSocketError(Exception):
    """WebSocket protocol parser error."""
    def __init__(self, code: int, message: str) -> None:
        self.code = ...
    
    def __str__(self) -> str:
        ...
    


class WSHandshakeError(Exception):
    """WebSocket protocol handshake error."""
    ...


native_byteorder = sys.byteorder
_XOR_TABLE = [bytes(a ^ b for a in range(256)) for b in range(256)]
def _websocket_mask_python(mask: bytes, data: bytearray) -> None:
    """Websocket masking function.

    `mask` is a `bytes` object of length 4; `data` is a `bytearray`
    object of any length. The contents of `data` are masked with `mask`,
    as specified in section 5.3 of RFC 6455.

    Note that this function mutates the `data` argument.

    This pure-python implementation may be replaced by an optimized
    version when available.

    """
    ...

if NO_EXTENSIONS:
    _websocket_mask = _websocket_mask_python
else:
    ...
_WS_DEFLATE_TRAILING = bytes([0, 0, 255, 255])
_WS_EXT_RE = re.compile(r'^(?:;\s*(?:' r'(server_no_context_takeover)|' r'(client_no_context_takeover)|' r'(server_max_window_bits(?:=(\d+))?)|' r'(client_max_window_bits(?:=(\d+))?)))*$')
_WS_EXT_RE_SPLIT = re.compile(r'permessage-deflate([^,]+)?')
def ws_ext_parse(extstr: str, isserver: bool = ...) -> Tuple[int, bool]:
    ...

def ws_ext_gen(compress: int = ..., isserver: bool = ..., server_notakeover: bool = ...) -> str:
    ...

class WSParserState(IntEnum):
    READ_HEADER = ...
    READ_PAYLOAD_LENGTH = ...
    READ_PAYLOAD_MASK = ...
    READ_PAYLOAD = ...


class WebSocketReader:
    def __init__(self, queue: DataQueue[WSMessage], max_msg_size: int, compress: bool = ...) -> None:
        self.queue = ...
    
    def feed_eof(self) -> None:
        ...
    
    def feed_data(self, data: bytes) -> Tuple[bool, bytes]:
        ...
    
    def _feed_data(self, data: bytes) -> Tuple[bool, bytes]:
        ...
    
    def parse_frame(self, buf: bytes) -> List[Tuple[bool, Optional[int], bytearray, Optional[bool]]]:
        """Return the next frame from the socket."""
        ...
    


class WebSocketWriter:
    def __init__(self, protocol: BaseProtocol, transport: asyncio.Transport, *, use_mask: bool = ..., limit: int = ..., random: Any = ..., compress: int = ..., notakeover: bool = ...) -> None:
        self.protocol = ...
        self.transport = ...
        self.use_mask = ...
        self.randrange = ...
        self.compress = ...
        self.notakeover = ...
    
    async def _send_frame(self, message: bytes, opcode: int, compress: Optional[int] = ...) -> None:
        """Send a frame over the websocket with message as its payload."""
        ...
    
    async def pong(self, message: bytes = ...) -> None:
        """Send pong message."""
        ...
    
    async def ping(self, message: bytes = ...) -> None:
        """Send ping message."""
        ...
    
    async def send(self, message: Union[str, bytes], binary: bool = ..., compress: Optional[int] = ...) -> None:
        """Send a frame over the websocket with message as its payload."""
        ...
    
    async def close(self, code: int = ..., message: bytes = ...) -> None:
        """Close the websocket, sending the specified code and message."""
        ...
    


