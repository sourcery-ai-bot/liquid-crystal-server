"""
This type stub file was generated by pyright.
"""

import asyncio
import os
import pathlib
from typing import Any, Awaitable, Callable, IO, Optional, TYPE_CHECKING, Union
from .abc import AbstractStreamWriter
from .base_protocol import BaseProtocol
from .http_writer import StreamWriter
from .typedefs import LooseHeaders
from .web_response import StreamResponse
from .web_request import BaseRequest

__all__ = ('FileResponse', )
if TYPE_CHECKING:
    ...
_T_OnChunkSent = Optional[Callable[[bytes], Awaitable[None]]]
NOSENDFILE = bool(os.environ.get("AIOHTTP_NOSENDFILE"))
class SendfileStreamWriter(StreamWriter):
    def __init__(self, protocol: BaseProtocol, loop: asyncio.AbstractEventLoop, fobj: IO[Any], count: int, on_chunk_sent: _T_OnChunkSent = ...) -> None:
        ...
    
    def _write(self, chunk: bytes) -> None:
        ...
    
    def _sendfile_cb(self, fut: asyncio.Future[None], out_fd: int) -> None:
        ...
    
    def _do_sendfile(self, out_fd: int) -> bool:
        ...
    
    def _done_fut(self, out_fd: int, fut: asyncio.Future[None]) -> None:
        ...
    
    async def sendfile(self) -> None:
        ...
    
    async def write_eof(self, chunk: bytes = ...) -> None:
        ...
    


class FileResponse(StreamResponse):
    """A response object can be used to send files."""
    def __init__(self, path: Union[str, pathlib.Path], chunk_size: int = ..., status: int = ..., reason: Optional[str] = ..., headers: Optional[LooseHeaders] = ...) -> None:
        ...
    
    async def _sendfile_system(self, request: BaseRequest, fobj: IO[Any], count: int) -> AbstractStreamWriter:
        ...
    
    async def _sendfile_fallback(self, request: BaseRequest, fobj: IO[Any], count: int) -> AbstractStreamWriter:
        ...
    
    if hasattr(os, "sendfile") and not NOSENDFILE:
        _sendfile = ...
    else:
        _sendfile = ...
    async def prepare(self, request: BaseRequest) -> Optional[AbstractStreamWriter]:
        self.last_modified = ...
        self.content_length = ...
    


