from typing import Optional, Union


def b64encode(s: bytes, altchars: Optional[bytes] = ...) -> bytes: ...
def b64decode(
    s: Union[bytes, str], altchars: Optional[bytes] = ..., validate: bool = ...
) -> bytes: ...
def standard_b64encode(s: bytes) -> bytes: ...
def standard_b64decode(s: Union[bytes, str]) -> bytes: ...
def urlsafe_b64encode(s: bytes) -> bytes: ...
def urlsafe_b64decode(s: Union[bytes, str]) -> bytes: ...