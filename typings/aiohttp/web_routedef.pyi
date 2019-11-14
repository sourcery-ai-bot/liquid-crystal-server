"""
This type stub file was generated by pyright.
"""

import abc
import attr
from typing import Any, Awaitable, Callable, Iterator, List, Optional, Sequence, TYPE_CHECKING, Type, Union, overload
from .abc import AbstractView
from .typedefs import PathLike
from .web_urldispatcher import UrlDispatcher
from .web_request import Request
from .web_response import StreamResponse

if TYPE_CHECKING:
    ...
else:
    Request = StreamResponse = UrlDispatcher = None
__all__ = ('AbstractRouteDef', 'RouteDef', 'StaticDef', 'RouteTableDef', 'head', 'options', 'get', 'post', 'patch', 'put', 'delete', 'route', 'view', 'static')
class AbstractRouteDef(abc.ABC):
    @abc.abstractmethod
    def register(self, router: UrlDispatcher) -> None:
        ...
    


_SimpleHandler = Callable[[Request], Awaitable[StreamResponse]]
_HandlerType = Union[Type[AbstractView], _SimpleHandler]
@attr.s(frozen=True, repr=False, slots=True)
class RouteDef(AbstractRouteDef):
    method = ...
    path = ...
    handler = ...
    kwargs = ...
    def __repr__(self) -> str:
        ...
    
    def register(self, router: UrlDispatcher) -> None:
        ...
    


@attr.s(frozen=True, repr=False, slots=True)
class StaticDef(AbstractRouteDef):
    prefix = ...
    path = ...
    kwargs = ...
    def __repr__(self) -> str:
        ...
    
    def register(self, router: UrlDispatcher) -> None:
        ...
    


def route(method: str, path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def head(path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def options(path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def get(path: str, handler: _HandlerType, *, name: Optional[str] = ..., allow_head: bool = ..., **kwargs: Any) -> RouteDef:
    ...

def post(path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def put(path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def patch(path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def delete(path: str, handler: _HandlerType, **kwargs: Any) -> RouteDef:
    ...

def view(path: str, handler: Type[AbstractView], **kwargs: Any) -> RouteDef:
    ...

def static(prefix: str, path: PathLike, **kwargs: Any) -> StaticDef:
    ...

_Deco = Callable[[_HandlerType], _HandlerType]
class RouteTableDef(Sequence[AbstractRouteDef]):
    """Route definition table"""
    def __init__(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @overload
    def __getitem__(self, index: int) -> AbstractRouteDef:
        ...
    
    @overload
    def __getitem__(self, index: slice) -> List[AbstractRouteDef]:
        ...
    
    def __getitem__(self, index):
        ...
    
    def __iter__(self) -> Iterator[AbstractRouteDef]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, item: object) -> bool:
        ...
    
    def route(self, method: str, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def head(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def get(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def post(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def put(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def patch(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def delete(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def view(self, path: str, **kwargs: Any) -> _Deco:
        ...
    
    def static(self, prefix: str, path: PathLike, **kwargs: Any) -> None:
        ...
    


