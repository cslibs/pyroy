import ipaddress
import re
import uuid

import hypothesis
from hypothesis import strategies

from pyroy import regexp


@hypothesis.given(strategies.ip_addresses(v=4))
def test_ipv4(ipv4_address: ipaddress.IPv4Address) -> None:
    string = str(ipv4_address)
    assert re.search(regexp.IPV4, string)


@hypothesis.given(strategies.ip_addresses(v=4))
def test_ipv4_binary(ipv4_address: ipaddress.IPv4Address) -> None:
    bytes_ = str(ipv4_address).encode('ASCII')
    assert re.search(regexp.IPV4_BINARY, bytes_)


@hypothesis.given(strategies.ip_addresses(v=6))
def test_ipv6(ipv6_address: ipaddress.IPv6Address) -> None:
    string = str(ipv6_address)
    assert re.search(regexp.IPV6, string)


@hypothesis.given(strategies.ip_addresses(v=6))
def test_ipv6_binary(ipv6_address: ipaddress.IPv6Address) -> None:
    bytes_ = str(ipv6_address).encode('ASCII')
    assert re.search(regexp.IPV6_BINARY, bytes_)


@hypothesis.given(strategies.uuids(version=4))
def test_uuid4(uuid_: uuid.UUID) -> None:
    bytes_ = str(uuid_)
    assert re.search(regexp.UUID4, bytes_)


@hypothesis.given(strategies.uuids(version=4))
def test_uuid4_binary(uuid_: uuid.UUID) -> None:
    bytes_ = str(uuid_).encode('ASCII')
    assert re.search(regexp.UUID4_BINARY, bytes_)
