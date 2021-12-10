import re
from typing import AnyStr, Generic

from pyroy.typedefs import Checker


class RegExpMatch(Checker, Generic[AnyStr]):
    def __init__(self, pattern: AnyStr, flags: int = 0) -> None:
        self.pattern: re.Pattern[AnyStr] = re.compile(pattern, flags)

    def __call__(self, checkable: AnyStr) -> bool:
        return bool(re.match(self.pattern, checkable))
