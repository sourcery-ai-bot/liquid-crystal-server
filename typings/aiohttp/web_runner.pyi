"""
This type stub file was generated by pyright.
"""

import socket
from abc import ABC, abstractmethod
from typing import Any, List, Optional, Set
from .web_app import Application
from .web_server import Server

__all__ = ('BaseSite', 'TCPSite', 'UnixSite', 'NamedPipeSite', 'SockSite', 'BaseRunner', 'AppRunner', 'ServerRunner', 'GracefulExit')
class GracefulExit(SystemExit):
    code = ...


def _raise_graceful_exit() -> None:
    ...

class BaseSite(ABC):
    __slots__ = ...
    def __init__(self, runner: BaseRunner, *, shutdown_timeout: float = ..., ssl_context: Optional[SSLContext] = ..., backlog: int = ...) -> None:
        ...
    
    @property
    @abstractmethod
    def name(self) -> str:
        ...
    
    @abstractmethod
    async def start(self) -> None:
        ...
    
    async def stop(self) -> None:
        ...
    


class TCPSite(BaseSite):
    __slots__ = ...
    def __init__(self, runner: BaseRunner, host: str = ..., port: int = ..., *, shutdown_timeout: float = ..., ssl_context: Optional[SSLContext] = ..., backlog: int = ..., reuse_address: Optional[bool] = ..., reuse_port: Optional[bool] = ...) -> None:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    async def start(self) -> None:
        ...
    


class UnixSite(BaseSite):
    __slots__ = ...
    def __init__(self, runner: BaseRunner, path: str, *, shutdown_timeout: float = ..., ssl_context: Optional[SSLContext] = ..., backlog: int = ...) -> None:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    async def start(self) -> None:
        ...
    


class NamedPipeSite(BaseSite):
    __slots__ = ...
    def __init__(self, runner: BaseRunner, path: str, *, shutdown_timeout: float = ...) -> None:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    async def start(self) -> None:
        ...
    


class SockSite(BaseSite):
    __slots__ = ...
    def __init__(self, runner: BaseRunner, sock: socket.socket, *, shutdown_timeout: float = ..., ssl_context: Optional[SSLContext] = ..., backlog: int = ...) -> None:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    async def start(self) -> None:
        ...
    


class BaseRunner(ABC):
    __slots__ = ...
    def __init__(self, *, handle_signals: bool = ..., **kwargs: Any) -> None:
        ...
    
    @property
    def server(self) -> Optional[Server]:
        ...
    
    @property
    def addresses(self) -> List[str]:
        ...
    
    @property
    def sites(self) -> Set[BaseSite]:
        ...
    
    async def setup(self) -> None:
        ...
    
    @abstractmethod
    async def shutdown(self) -> None:
        ...
    
    async def cleanup(self) -> None:
        ...
    
    @abstractmethod
    async def _make_server(self) -> Server:
        ...
    
    @abstractmethod
    async def _cleanup_server(self) -> None:
        ...
    
    def _reg_site(self, site: BaseSite) -> None:
        ...
    
    def _check_site(self, site: BaseSite) -> None:
        ...
    
    def _unreg_site(self, site: BaseSite) -> None:
        ...
    


class ServerRunner(BaseRunner):
    """Low-level web server runner"""
    __slots__ = ...
    def __init__(self, web_server: Server, *, handle_signals: bool = ..., **kwargs: Any) -> None:
        ...
    
    async def shutdown(self) -> None:
        ...
    
    async def _make_server(self) -> Server:
        ...
    
    async def _cleanup_server(self) -> None:
        ...
    


class AppRunner(BaseRunner):
    """Web Application runner"""
    __slots__ = ...
    def __init__(self, app: Application, *, handle_signals: bool = ..., **kwargs: Any) -> None:
        ...
    
    @property
    def app(self) -> Application:
        ...
    
    async def shutdown(self) -> None:
        ...
    
    async def _make_server(self) -> Server:
        ...
    
    async def _cleanup_server(self) -> None:
        ...
    

