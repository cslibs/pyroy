from pyroy import typedefs


def test_async_checker_type() -> None:
    typedefs.AsyncCheckerType


def test_sync_checker_type() -> None:
    typedefs.SyncCheckerType


def test_checker_type() -> None:
    typedefs.CheckerType
