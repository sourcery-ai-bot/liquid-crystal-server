"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Any, Optional, Tuple
from .base_protocol import BaseProtocol
from .helpers import BaseTimerContext
from .http import RawResponseMessage
from .streams import DataQueue, StreamReader

class ResponseHandler(BaseProtocol, DataQueue[Tuple[RawResponseMessage, StreamReader]]):
    """Helper class to adapt between Protocol and StreamReader."""
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        ...
    
    @property
    def upgraded(self) -> bool:
        ...
    
    @property
    def should_close(self) -> bool:
        ...
    
    def force_close(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def is_connected(self) -> bool:
        ...
    
    def connection_lost(self, exc: Optional[BaseException]) -> None:
        ...
    
    def eof_received(self) -> None:
        ...
    
    def pause_reading(self) -> None:
        ...
    
    def resume_reading(self) -> None:
        ...
    
    def set_exception(self, exc: BaseException) -> None:
        ...
    
    def set_parser(self, parser: Any, payload: Any) -> None:
        ...
    
    def set_response_params(self, *, timer: BaseTimerContext = ..., skip_payload: bool = ..., read_until_eof: bool = ..., auto_decompress: bool = ..., read_timeout: Optional[float] = ...) -> None:
        ...
    
    def _drop_timeout(self) -> None:
        ...
    
    def _reschedule_timeout(self) -> None:
        ...
    
    def _on_read_timeout(self) -> None:
        ...
    
    def data_received(self, data: bytes) -> None:
        ...
    


