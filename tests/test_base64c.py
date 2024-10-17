import base64c
import base64
import time
import os
import pytest
import random
from typing import Callable, List, Tuple, Literal, TypeAlias
from string import ascii_letters, digits


TestKey: TypeAlias = Literal["Small text", "Large text", "Binary data","JPEG image","PNG image","MP3 audio"]


def random_text(length: int) -> bytes:
    return "".join(random.choice(ascii_letters + digits) for _ in range(length)).encode()

def random_binary(length: int) -> bytes:
    return os.urandom(length)

def generate_test_data() -> List[Tuple[TestKey, bytes]]:
    return [
        ("Small text", random_text(100)),
        ("Large text", random_text(1000000)),
        ("Binary data", random_binary(1000000)),
        ("JPEG image", open("assets/sample.jpeg", "rb").read()),
        ("PNG image", open("assets/sample.png", "rb").read()),
        ("MP3 audio", open("assets/sample.mp3", "rb").read()),
    ]

def benchmark(func: Callable, data: bytes, iterations: int = 100) -> float:
    start = time.time()
    for _ in range(iterations):
        func(data)
    end = time.time()
    return end - start

# Test data fixture
@pytest.fixture(scope="module")
def test_data():
    return generate_test_data()

# Fixture to store results
@pytest.fixture(scope="module")
def performance_results():
    return {}

# Correctness tests
@pytest.mark.parametrize(
    "func_name",
    [
        "b64encode", "b64decode",
        "standard_b64encode", "standard_b64decode",
        "urlsafe_b64encode", "urlsafe_b64decode",
    ],
)
def test_correctness(func_name, test_data):
    for name, data in test_data:
        stdlib_func = getattr(base64, func_name)
        base64c_func = getattr(base64c, func_name)

        if "decode" in func_name:
            data = getattr(base64, func_name.replace("decode", "encode"))(data)

        stdlib_result = stdlib_func(data)
        base64c_result = base64c_func(data)

        assert stdlib_result == base64c_result, f"{func_name} failed for {name}"

# Performance tests
@pytest.mark.parametrize(
    "func_name",
    [
        "b64encode", "b64decode",
        "standard_b64encode", "standard_b64decode",
        "urlsafe_b64encode", "urlsafe_b64decode",
    ],
)
def test_performance(func_name, test_data, performance_results):
    for name, data in test_data:
        stdlib_func = getattr(base64, func_name)
        base64c_func = getattr(base64c, func_name)

        if "decode" in func_name:
            data = getattr(base64, func_name.replace("decode", "encode"))(data)

        # Adjust iterations for large data
        iterations = 10 if len(data) > 100000 else 100

        stdlib_time = benchmark(stdlib_func, data, iterations)
        base64c_time = benchmark(base64c_func, data, iterations)
        speedup = stdlib_time / base64c_time

        # Store results in the performance_results fixture
        if name not in performance_results:
            performance_results[name] = {}
        performance_results[name][func_name] = {
            "stdlib_time": stdlib_time,
            "base64c_time": base64c_time,
            "speedup": speedup,
        }

        assert speedup > 1, f"{func_name} with {name} is not faster than stdlib"