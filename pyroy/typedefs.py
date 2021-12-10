from collections.abc import Callable, Coroutine
from typing import Any, Protocol, Type, runtime_checkable

AsyncCheckerType = Coroutine[Any, Any, bool]
SyncCheckerType = Callable[..., bool]
CheckerType = AsyncCheckerType | SyncCheckerType


@runtime_checkable
class Checker(Protocol):
    def __call__(self, checkable: Any) -> bool:
        ...


@runtime_checkable
class Validator(Protocol):
    checker: Checker
    error: Type[Exception]

    def __init__(self, checker: Any, error: Type[Exception]) -> None:
        self.checker = checker
        self.error = error

    def __call__(self, validable: Any) -> None:
        if self.checker(validable) is False:
            raise self.error(validable)
        return None
