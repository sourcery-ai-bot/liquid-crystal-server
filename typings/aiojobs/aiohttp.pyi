"""
This type stub file was generated by pyright.
"""

__all__ = ('setup', 'spawn', 'get_scheduler', 'get_scheduler_from_app', 'atomic')
from typing import Callable


def get_scheduler(request):
    ...


def get_scheduler_from_app(app):
    ...


def get_scheduler_from_request(request):
    ...


async def spawn(request, coro):
    ...


def atomic(coro: Callable) -> Callable:
    ...


def setup(app, **kwargs):
    ...
