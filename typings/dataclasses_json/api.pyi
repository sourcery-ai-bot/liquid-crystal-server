"""
This type stub file was generated by pyright.
"""

import abc
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar, Union
from marshmallow.fields import Field as MarshmallowField
from dataclasses_json.core import Json
from dataclasses_json.mm import JsonData, SchemaType

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
Fields = List[Tuple[str, Any]]
class LetterCase(Enum):
    CAMEL = ...
    KEBAB = ...
    SNAKE = ...
    PASCAL = ...


def config(metadata: dict = ..., *, encoder: callable = ..., decoder: callable = ..., mm_field: MarshmallowField = ..., letter_case: Callable[[str], str] = ..., field_name: str = ...) -> Dict[str, dict]:
    ...

class DataClassJsonMixin(abc.ABC):
    """
    DataClassJsonMixin is an ABC that functions as a Mixin.

    As with other ABCs, it should not be instantiated directly.
    """
    dataclass_json_config = ...
    def to_json(self, *, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., indent: Optional[Union[int, str]] = ..., separators: Tuple[str, str] = ..., default: Callable = ..., sort_keys: bool = ..., **kw) -> str:
        ...
    
    @classmethod
    def from_json(cls: Type[A], s: JsonData, *, encoding: Optional[Any] = ..., parse_float: Optional[Any] = ..., parse_int: Optional[Any] = ..., parse_constant: Optional[Any] = ..., infer_missing: bool = ..., **kw) -> A:
        ...
    
    @classmethod
    def from_dict(cls: Type[A], kvs: Json, *, infer_missing: bool = ...) -> A:
        ...
    
    def to_dict(self, encode_json: bool = ...):
        ...
    
    @classmethod
    def schema(cls: Type[A], *, infer_missing: bool = ..., only: Optional[Any] = ..., exclude=..., many: bool = ..., context: Optional[Any] = ..., load_only=..., dump_only=..., partial: bool = ..., unknown: Optional[Any] = ...) -> SchemaType:
        ...
    


def dataclass_json(_cls: Optional[Any] = ..., *, letter_case: Optional[Any] = ...):
    """
    Based on the code in the `dataclasses` module to handle optional-parens
    decorators. See example below:

    @dataclass_json
    @dataclass_json(letter_case=Lettercase.CAMEL)
    class Example:
        ...
    """
    ...

def _process_class(cls, letter_case):
    ...

