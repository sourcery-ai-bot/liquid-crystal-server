"""
This type stub file was generated by pyright.
"""

import asyncio
import collections
from typing import Awaitable, Callable, Optional
from multidict import CIMultiDict
from .abc import AbstractStreamWriter
from .base_protocol import BaseProtocol

"""Http related parsers and protocol."""
__all__ = ('StreamWriter', 'HttpVersion', 'HttpVersion10', 'HttpVersion11')
HttpVersion = collections.namedtuple('HttpVersion', ['major', 'minor'])
HttpVersion10 = HttpVersion(1, 0)
HttpVersion11 = HttpVersion(1, 1)
_T_OnChunkSent = Optional[Callable[[bytes], Awaitable[None]]]
class StreamWriter(AbstractStreamWriter):
    def __init__(self, protocol: BaseProtocol, loop: asyncio.AbstractEventLoop, on_chunk_sent: _T_OnChunkSent = ...) -> None:
        self.loop = ...
        self.length = ...
        self.chunked = ...
        self.buffer_size = ...
        self.output_size = ...
    
    @property
    def transport(self) -> Optional[asyncio.Transport]:
        ...
    
    @property
    def protocol(self) -> BaseProtocol:
        ...
    
    def enable_chunking(self) -> None:
        self.chunked = ...
    
    def enable_compression(self, encoding: str = ...) -> None:
        ...
    
    def _write(self, chunk: bytes) -> None:
        ...
    
    async def write(self, chunk: bytes, *, drain: bool = ..., LIMIT: int = ...) -> None:
        """Writes chunk of data to a stream.

        write_eof() indicates end of stream.
        writer can't be used after write_eof() method being called.
        write() return drain future.
        """
        ...
    
    async def write_headers(self, status_line: str, headers: CIMultiDict[str]) -> None:
        """Write request/response status and headers."""
        ...
    
    async def write_eof(self, chunk: bytes = ...) -> None:
        ...
    
    async def drain(self) -> None:
        """Flush the write buffer.

        The intended use is to write

          await w.write(data)
          await w.drain()
        """
        ...
    


def _py_serialize_headers(status_line: str, headers: CIMultiDict[str]) -> bytes:
    ...

_serialize_headers = _py_serialize_headers