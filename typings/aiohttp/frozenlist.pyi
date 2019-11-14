"""
This type stub file was generated by pyright.
"""

from typing import Generic, Iterable, Iterator, List, MutableSequence, Optional, TypeVar, Union, overload

_T = TypeVar('_T')
_Arg = Union[List[_T], Iterable[_T]]
class FrozenList(MutableSequence[_T], Generic[_T]):
    def __init__(self, items: Optional[_Arg[_T]] = ...) -> None:
        ...
    
    @property
    def frozen(self) -> bool:
        ...
    
    def freeze(self) -> None:
        ...
    
    @overload
    def __getitem__(self, i: int) -> _T:
        ...
    
    @overload
    def __getitem__(self, s: slice) -> FrozenList[_T]:
        ...
    
    @overload
    def __setitem__(self, i: int, o: _T) -> None:
        ...
    
    @overload
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None:
        ...
    
    @overload
    def __delitem__(self, i: int) -> None:
        ...
    
    @overload
    def __delitem__(self, i: slice) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[_T]:
        ...
    
    def __reversed__(self) -> Iterator[_T]:
        ...
    
    def __eq__(self, other: object) -> bool:
        ...
    
    def __le__(self, other: FrozenList[_T]) -> bool:
        ...
    
    def __ne__(self, other: object) -> bool:
        ...
    
    def __lt__(self, other: FrozenList[_T]) -> bool:
        ...
    
    def __ge__(self, other: FrozenList[_T]) -> bool:
        ...
    
    def __gt__(self, other: FrozenList[_T]) -> bool:
        ...
    
    def insert(self, pos: int, item: _T) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    


CFrozenList = PyFrozenList = FrozenList
