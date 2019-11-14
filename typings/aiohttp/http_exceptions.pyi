"""
This type stub file was generated by pyright.
"""

from typing import Optional, Union
from .typedefs import _CIMultiDict

"""Low-level http related exceptions."""
__all__ = ('HttpProcessingError', )
class HttpProcessingError(Exception):
    """HTTP error.

    Shortcut for raising HTTP errors with custom code, message and headers.

    code: HTTP Error code.
    message: (optional) Error message.
    headers: (optional) Headers to be sent in response, a list of pairs
    """
    code = ...
    message = ...
    headers = ...
    def __init__(self, *, code: Optional[int] = ..., message: str = ..., headers: Optional[_CIMultiDict] = ...) -> None:
        self.headers = ...
        self.message = ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    


class BadHttpMessage(HttpProcessingError):
    code = ...
    message = ...
    def __init__(self, message: str, *, headers: Optional[_CIMultiDict] = ...) -> None:
        self.args = ...
    


class HttpBadRequest(BadHttpMessage):
    code = ...
    message = ...


class PayloadEncodingError(BadHttpMessage):
    """Base class for payload errors"""
    ...


class ContentEncodingError(PayloadEncodingError):
    """Content encoding error."""
    ...


class TransferEncodingError(PayloadEncodingError):
    """transfer encoding error."""
    ...


class ContentLengthError(PayloadEncodingError):
    """Not enough data for satisfy content length header."""
    ...


class LineTooLong(BadHttpMessage):
    def __init__(self, line: str, limit: str = ..., actual_size: str = ...) -> None:
        self.args = ...
    


class InvalidHeader(BadHttpMessage):
    def __init__(self, hdr: Union[bytes, str]) -> None:
        self.hdr = ...
        self.args = ...
    


class BadStatusLine(BadHttpMessage):
    def __init__(self, line: str = ...) -> None:
        self.args = ...
        self.line = ...
    
    __str__ = ...
    __repr__ = ...


class InvalidURLError(BadHttpMessage):
    ...

