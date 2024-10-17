LICENSE 1072 9640d08a26eb73a7c4c6afe7548e3ddd1bcc4ef8e178e3c2419b4000846e25a3 MIT License

Copyright (c) 2024 Oscar Bahamonde

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

.pytest_cache/CACHEDIR.TAG 191 37dc88ef9a0abeddbe81053a6dd8fdfb13afb613045ea1eb4a5c815a74a3bde4 Signature: 8a477f597d28d172789f06886806bc55
# This file is a cache directory tag created by pytest.
# For information about cache directory tags, see:
#	https://bford.info/cachedir/spec.html

.pytest_cache/README.md 302 73fd6fccdd802c419a6b2d983d6c3173b7da97558ac4b589edec2dfe443db9ad # pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

.pytest_cache/.gitignore 37 3ed731b65d06150c138e2dadb0be0697550888a6b47eb8c45ecc9adba8b8e9bd # Created by pytest automatically.
*

.pytest_cache/v/cache/nodeids 2 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 []
.pytest_cache/v/cache/stepwise 2 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 []
Dockerfile 158 1e25b59976b0aa123f73ec327907e4399a7c79fba9e055669c4bce5a18f74a79 FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install --no-root --no-dev

CMD ["pytest", "--html=test_report.html"]	






Makefile 1586 d6a6b3cb9b443b1cd7866399a84101d65453fbbae44d83311dca70e0fae46fab # Makefile for base64c project


# Variables
PACKAGE_NAME = base64c
PYTHON = python
BUILD_DIR = dist
SOURCE_DIR = src/base64c
SOURCE_FILES = $(wildcard $(SOURCE_DIR)/*.c)

# Default target
.PHONY: all
all: build

# Build the package using setuptools
.PHONY: build
build:
	$(PYTHON) setup.py build_ext --inplace

# Clean up build artifacts
.PHONY: clean
clean:
	@echo "Cleaning up build artifacts..."
	rm -rf $(BUILD_DIR) build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.so" -delete

.PHONY: test
test:
	@echo "Running tests..."
	pytest -v

.PHONY: install
install:
	@echo "Installing the package locally..."
	pip install -e .

.PHONY: dist
dist: clean
	@echo "Building source distribution..."
	$(PYTHON) setup.py sdist

.PHONY: publish
publish: dist
	@echo "Publishing the package to PyPI..."
	@if [ -z "$(PYPI_TOKEN)" ]; then \
		echo "Error: PYPI_TOKEN environment variable is not set"; \
		exit 1; \
	fi
	twine upload dist/* -u __token__ -p $(PYPI_TOKEN)

.PHONY: help
help:
	@echo "Makefile for the $(PACKAGE_NAME) project"
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all              Build the package (default target)"
	@echo "  build            Build the package using setuptools"
	@echo "  clean            Clean up build artifacts"
	@echo "  test             Run tests"
	@echo "  install          Install the package locally"
	@echo "  dist             Build source distribution"
	@echo "  publish          Publish the package to PyPI (requires PYPI_TOKEN env var)"
	@echo "  help             Show this help message"
pyproject.toml 1597 e38c9c5317360beb66b502ba6bfb3a7bb03bdce742418630511f6bc282569d36 [project]
name = "base64c"
version = "0.0.9"
description = "Fast Base64 encoding/decoding with SSE2 and VSX optimizations"
authors = [{name = "Oscar Bahamonde", email = "oscar.bahamonde@indiecloud.co"}]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: C",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]
requires-python = ">=3.8"
readme = "README.md"

[tool.poetry]
name = "base64c"
version = "0.0.9"
description = "Fast Base64 encoding/decoding with SSE2 and VSX optimizations."
authors = ["obahamonde <oscar.bahamonde@indiecloud.co>"]
readme = "README.md"
packages = [{include = "base64c", from = "src"}]

[tool.poetry.group.dev.dependencies]
pytest = "^8.3.3"

[project.optional-dependencies]
dev = ["pytest", "pyright", "isort", "black","pytest-html","setuptools"]

[tool.poetry.dependencies]
python = "^3.8"

[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
packages = ["base64c"]
package-dir = {"base64c" = "src/base64c"}

[tool.setuptools.package-data]
base64c = ["*.pyi"]

[tool.setuptools_scm]
data.md 0 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 
tests/test_base64c.py 3178 e997cd9797f1d8a794c1d418e74c6a6bccb211b5135007763d2871936fe33d37 import base64c
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
tests/__init__.py 428 8bea32778b09c08c1cdd9a0fba9ac47ac2d87d185bd184938fbbca9741dd9611 from typing import Optional, Union


def b64encode(s: bytes, altchars: Optional[bytes] = ...) -> bytes: ...
def b64decode(
    s: Union[bytes, str], altchars: Optional[bytes] = ..., validate: bool = ...
) -> bytes: ...
def standard_b64encode(s: bytes) -> bytes: ...
def standard_b64decode(s: Union[bytes, str]) -> bytes: ...
def urlsafe_b64encode(s: bytes) -> bytes: ...
def urlsafe_b64decode(s: Union[bytes, str]) -> bytes: ...
tests/test_base64c.c 4704 cc88f391be1861ebd05d7a6ff6f1a3314011c534764003860e3334e703193f53 #include <stdio.h>
#include <string.h>
#include <time.h>
#include <assert.h>
#include "base64c.h"

#define TEST_CASES 6
#define LARGE_SIZE 1000000
#define BENCHMARK_ITERATIONS 1000

// Test cases
const char* test_strings[TEST_CASES] = {
    "",
    "f",
    "fo",
    "foo",
    "foob",
    "fooba",
};

const char* expected_standard[TEST_CASES] = {
    "",
    "Zg==",
    "Zm8=",
    "Zm9v",
    "Zm9vYg==",
    "Zm9vYmE=",
};

const char* expected_urlsafe[TEST_CASES] = {
    "",
    "Zg==",
    "Zm8=",
    "Zm9v",
    "Zm9vYg==",
    "Zm9vYmE=",
};

void test_encoding() {
    printf("Testing encoding...\n");
    for (int i = 0; i < TEST_CASES; i++) {
        PyObject* args = Py_BuildValue("y#", test_strings[i], strlen(test_strings[i]));
        PyObject* result = b64encode(NULL, args);
        assert(result != NULL);
        
        const char* encoded = PyBytes_AsString(result);
        assert(encoded != NULL);
        
        printf("Input: %s\n", test_strings[i]);
        printf("Encoded: %s\n", encoded);
        printf("Expected: %s\n", expected_standard[i]);
        assert(strcmp(encoded, expected_standard[i]) == 0);
        
        Py_DECREF(result);
        Py_DECREF(args);
    }
    printf("Encoding tests passed.\n\n");
}

void test_decoding() {
    printf("Testing decoding...\n");
    for (int i = 0; i < TEST_CASES; i++) {
        PyObject* args = Py_BuildValue("y#", expected_standard[i], strlen(expected_standard[i]));
        PyObject* result = b64decode(NULL, args);
        assert(result != NULL);
        
        const char* decoded = PyBytes_AsString(result);
        assert(decoded != NULL);
        
        printf("Input: %s\n", expected_standard[i]);
        printf("Decoded: %s\n", decoded);
        printf("Expected: %s\n", test_strings[i]);
        assert(strcmp(decoded, test_strings[i]) == 0);
        
        Py_DECREF(result);
        Py_DECREF(args);
    }
    printf("Decoding tests passed.\n\n");
}

void test_urlsafe() {
    printf("Testing URL-safe encoding and decoding...\n");
    for (int i = 0; i < TEST_CASES; i++) {
        PyObject* args = Py_BuildValue("y#", test_strings[i], strlen(test_strings[i]));
        PyObject* encoded = urlsafe_b64encode(NULL, args);
        assert(encoded != NULL);
        
        const char* encoded_str = PyBytes_AsString(encoded);
        assert(encoded_str != NULL);
        
        printf("Input: %s\n", test_strings[i]);
        printf("URL-safe encoded: %s\n", encoded_str);
        printf("Expected: %s\n", expected_urlsafe[i]);
        assert(strcmp(encoded_str, expected_urlsafe[i]) == 0);
        
        PyObject* decoded = urlsafe_b64decode(NULL, Py_BuildValue("y#", encoded_str, strlen(encoded_str)));
        assert(decoded != NULL);
        
        const char* decoded_str = PyBytes_AsString(decoded);
        assert(decoded_str != NULL);
        
        printf("Decoded: %s\n", decoded_str);
        assert(strcmp(decoded_str, test_strings[i]) == 0);
        
        Py_DECREF(encoded);
        Py_DECREF(decoded);
        Py_DECREF(args);
    }
    printf("URL-safe tests passed.\n\n");
}

void benchmark() {
    printf("Running benchmarks...\n");
    char* large_input = malloc(LARGE_SIZE);
    memset(large_input, 'A', LARGE_SIZE);
    
    PyObject* args = Py_BuildValue("y#", large_input, LARGE_SIZE);
    
    clock_t start, end;
    double cpu_time_used;
    
    // Benchmark encoding
    start = clock();
    for (int i = 0; i < BENCHMARK_ITERATIONS; i++) {
        PyObject* result = b64encode(NULL, args);
        Py_DECREF(result);
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Encoding %d times took %f seconds\n", BENCHMARK_ITERATIONS, cpu_time_used);
    
    // Benchmark decoding
    PyObject* encoded = b64encode(NULL, args);
    PyObject* decode_args = Py_BuildValue("y#", PyBytes_AsString(encoded), PyBytes_Size(encoded));
    
    start = clock();
    for (int i = 0; i < BENCHMARK_ITERATIONS; i++) {
        PyObject* result = b64decode(NULL, decode_args);
        Py_DECREF(result);
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Decoding %d times took %f seconds\n", BENCHMARK_ITERATIONS, cpu_time_used);
    
    Py_DECREF(encoded);
    Py_DECREF(decode_args);
    Py_DECREF(args);
    free(large_input);
    
    printf("Benchmarks completed.\n");
}

int main() {
    // Initialize Python
    Py_Initialize();
    
    // Run tests
    test_encoding();
    test_decoding();
    test_urlsafe();
    
    // Run benchmarks
    benchmark();
    
    // Finalize Python
    Py_Finalize();
    
    printf("All tests passed successfully.\n");
    return 0;
}
README.md 551 0bebeef721a2c414ad002a7fd532bcd2dea9f31ccd6407a7d06233e489a7a630 # Base64C

A faster base64 encoding/decoding library for Python, implemented in C with SSSE3 and VSX optimizations.

## Installation

```bash
pip install base64c
```

## Usage

```python

from base64c import b64encode, b64decode

print(b64encode(b"Hello, World!"))
print(b64decode(b64encode(b"Hello, World!")))
```

## License

MIT

## Performance

* 3-24x faster than the stdlib `base64` module.
* Performance increases with input size.
* Tested across different types and sizes of inputs.

<br>

![Table](assets/table.png)
![Chart](assets/chart.png)
setup.py 2450 cff0075447626095eb36f9ed8a6b8419ba5719e7eed57cd4364554ce1fefae70 from setuptools import setup, Extension
import platform
import sys
import os

# Determine the appropriate compiler flags based on the platform
extra_compile_args = ['-O3']  # Optimize for speed using -O3

# Add architecture-specific optimizations
machine = platform.machine().lower()

if machine in ('x86_64', 'amd64', 'i386', 'i686'):
    extra_compile_args.append('-msse2')  # Use SSE2 for x86 architectures
elif 'ppc' in machine or 'powerpc' in machine:
    extra_compile_args.extend(['-mvsx', '-mcpu=power8'])  # Use VSX for PowerPC architectures

# For macOS, specify the minimum deployment target
if sys.platform == 'darwin':
    extra_compile_args.append('-mmacosx-version-min=10.9')

# Define the C extension module
base64c_module = Extension(
    'base64c.base64c',  # This ensures the .so file is placed in the base64c directory
    sources=[os.path.join('base64c', 'base64c.c')],  # Path to the C source file
    extra_compile_args=extra_compile_args
)

# Read the README file for the long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

# Setup configuration
setup(
    name='base64c',
    version='0.0.5',
    description='Fast Base64 encoding/decoding with SSE2 and VSX optimizations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Oscar Bahamonde',
    author_email="oscar.bahamonde@indiecloud.co",
    url='https://github.com/obahamonde/base64c',
    ext_modules=[base64c_module],
    packages=['base64c'],
    package_dir={'base64c': 'src/base64c'},  # Specify the directory for Python package
    include_package_data=True,
    options={'bdist_wheel': {'universal': True}},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: C',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.8',
    extras_require={
        'dev': ['pytest', 'pyright', 'isort', 'black'],
    }
)
cli.py 1293 6eae3273b14b2bc3133693af5838525955ff4f4a6cb8bf545c46390f154a9be6 from __future__ import annotations
import typing as tp
import argparse
import os
import pathlib
import hashlib
import base64
import sys
from dataclasses import dataclass, field

@dataclass
class Node:
    path: pathlib.Path = field(repr=False)
    size: int = field(repr=False)
    hash: str = field(repr=False)
    content: tp.Union[str,Node] = field(repr=False)

    @classmethod
    def from_path(cls, path: pathlib.Path, use_base64: bool = False) -> tp.Generator[Node, None, None]:
        for path in path.iterdir():
            if path.is_dir():
                yield from Node.from_path(path, use_base64)
            else:
                try:
                    content = path.read_text()
                except:
                    if use_base64:
                        content = base64.b64encode(path.read_bytes()).decode()
                    else:
                        content = "[Binary]"
                yield Node(path, path.stat().st_size, hashlib.sha256(content.encode()).hexdigest(), content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path)
    args = parser.parse_args()
    for node in Node.from_path(args.path):
        print(node.path, node.size, node.hash, node.content)

if __name__ == "__main__":
    main()

base64c/build.py 1725 4cb056b58775fe8c362ebbfe68da10df6bc9a1e91b728c41f85facfc1bcb5574 import os
import sys
from setuptools import Extension, setup
from setuptools.dist import Distribution
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    def run(self):
        build_ext.run(self)

def build(setup_kwargs):
    print("Starting build process...")
    
    # Define the C extension module
    base64c_module = Extension(
        'base64c.base64c',
        sources=[os.path.join('base64c', 'base64c.c')],
        extra_compile_args=['-O3', '-msse2'] if sys.platform != "darwin" else ['-O3']
    )

    # Create a distribution with our extension module
    dist = Distribution({'name': 'base64c', 'ext_modules': [base64c_module]})
    
    # Ensure the build_ext command is available
    dist.cmdclass['build_ext'] = BuildExt

    # Build the extension
    cmd = BuildExt(dist)
    cmd.ensure_finalized()
    cmd.run()

    # Specify the correct directory for the built extension
    build_dir = os.path.abspath(cmd.build_lib)
    
    print(f"Extension built in: {build_dir}")
    print(f"Files in build directory: {os.listdir(build_dir)}")

    # Update setup_kwargs
    setup_kwargs.update({
        'ext_modules': [base64c_module],
        'cmdclass': {'build_ext': BuildExt},
        'package_data': {'base64c': ['*.so', '*.pyd']},
        'include_package_data': True,
    })

    print("Build process completed.")

if __name__ == "__main__":
    setup(
        name='base64c',
        version='0.0.5',
        packages=['base64c'],
        package_dir={'base64c': 'src/base64c'},
        ext_modules=[Extension('base64c.base64c', sources=[os.path.join('base64c', 'base64c.c')])],
        cmdclass={'build_ext': BuildExt},
    )
    print("Setup completed when run directly.")
base64c/base64c.c 6468 4731219e15d35f4a9f4a8aebe17efa4e94f5b5b2965cce84fe74d74abde9525c #define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <immintrin.h>

static const uint8_t base64_table[64] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
static const uint8_t base64_urlsafe_table[64] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";

static const uint8_t base64_decode_table[256] = {
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 64, 64, 64, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 64, 64, 64, 64, 64,
    64,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 64, 64, 64, 64,
    64, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64
};
static PyObject* encode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* table) {
    Py_ssize_t output_len = ((input_len + 2) / 3) * 4;
    PyObject* output = PyBytes_FromStringAndSize(NULL, output_len);
    if (!output)
        return NULL;

    uint8_t* out = (uint8_t*)PyBytes_AS_STRING(output);

    Py_ssize_t i, j;
    for (i = 0, j = 0; i < input_len - 2; i += 3) {
        uint32_t n = (uint32_t)input[i] << 16 | (uint32_t)input[i + 1] << 8 | input[i + 2];
        out[j++] = table[(n >> 18) & 0x3F];
        out[j++] = table[(n >> 12) & 0x3F];
        out[j++] = table[(n >> 6) & 0x3F];
        out[j++] = table[n & 0x3F];
    }

    if (i < input_len) {
        uint32_t n = (uint32_t)input[i] << 16;
        if (i + 1 < input_len) n |= (uint32_t)input[i + 1] << 8;

        out[j++] = table[(n >> 18) & 0x3F];
        out[j++] = table[(n >> 12) & 0x3F];
        out[j++] = (i + 1 < input_len) ? table[(n >> 6) & 0x3F] : '=';
        out[j++] = '=';
    }

    return output;
}
static PyObject* decode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* decode_table) {
    if (input_len % 4 != 0) {
        PyErr_SetString(PyExc_ValueError, "Invalid base64-encoded string");
        return NULL;
    }

    Py_ssize_t output_len = input_len / 4 * 3;
    if (input[input_len - 1] == '=') output_len--;
    if (input[input_len - 2] == '=') output_len--;

    PyObject* output = PyBytes_FromStringAndSize(NULL, output_len);
    if (!output)
        return NULL;

    uint8_t* out = (uint8_t*)PyBytes_AS_STRING(output);

    Py_ssize_t i, j;
    for (i = 0, j = 0; i < input_len; i += 4) {
        uint32_t n = decode_table[input[i]] << 18 |
                     decode_table[input[i + 1]] << 12 |
                     decode_table[input[i + 2]] << 6 |
                     decode_table[input[i + 3]];

        out[j++] = (n >> 16) & 0xFF;
        if (input[i + 2] != '=')
            out[j++] = (n >> 8) & 0xFF;
        if (input[i + 3] != '=')
            out[j++] = n & 0xFF;
    }

    return output;
}

static PyObject* b64encode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return encode_base64(input, input_len, base64_table);
}

static PyObject* b64decode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return decode_base64(input, input_len, base64_decode_table);
}

static PyObject* standard_b64encode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return encode_base64(input, input_len, base64_table);
}

static PyObject* standard_b64decode(PyObject* self, PyObject* args) {
    const char* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "s#", &input, &input_len))
        return NULL;

    return decode_base64((const uint8_t*)input, input_len, base64_decode_table);
}

static PyObject* urlsafe_b64encode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return encode_base64(input, input_len, base64_urlsafe_table);
}

static PyObject* urlsafe_b64decode(PyObject* self, PyObject* args) {
    const char* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "s#", &input, &input_len))
        return NULL;

    char* modified_input = PyMem_Malloc(input_len);
    if (!modified_input) {
        return PyErr_NoMemory();
    }

    for (Py_ssize_t i = 0; i < input_len; i++) {
        if (input[i] == '-')
            modified_input[i] = '+';
        else if (input[i] == '_')
            modified_input[i] = '/';
        else
            modified_input[i] = input[i];
    }

    PyObject* result = decode_base64((const uint8_t*)modified_input, input_len, base64_decode_table);
    PyMem_Free(modified_input);
    return result;
}

static PyMethodDef Base64Methods[] = {
    {"b64encode", b64encode, METH_VARARGS, "Encode a byte string using Base64."},
    {"b64decode", b64decode, METH_VARARGS, "Decode a Base64 encoded byte string."},
    {"standard_b64encode", standard_b64encode, METH_VARARGS, "Encode a byte string using standard Base64."},
    {"standard_b64decode", standard_b64decode, METH_VARARGS, "Decode a standard Base64 encoded byte string."},
    {"urlsafe_b64encode", urlsafe_b64encode, METH_VARARGS, "Encode a byte string using URL-safe Base64."},
    {"urlsafe_b64decode", urlsafe_b64decode, METH_VARARGS, "Decode a URL-safe Base64 encoded byte string."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef base64cmodule = {
    PyModuleDef_HEAD_INIT,
    "base64c",
    "Fast Base64 encoding and decoding using AVX2.",
    -1,
    Base64Methods
};

PyMODINIT_FUNC PyInit_base64c(void) {
    return PyModule_Create(&base64cmodule);
}
base64c/base64c.h 1047 2a4458ba46dc5558adb33a6ca7a1e93d00b952b14787bab87ce67e7fc92cb0c1 #ifndef BASE64C_H
#define BASE64C_H

#include <Python.h>

// Function prototypes
static PyObject* b64encode(PyObject* self, PyObject* args);
static PyObject* b64decode(PyObject* self, PyObject* args);
static PyObject* standard_b64encode(PyObject* self, PyObject* args);
static PyObject* standard_b64decode(PyObject* self, PyObject* args);
static PyObject* urlsafe_b64encode(PyObject* self, PyObject* args);
static PyObject* urlsafe_b64decode(PyObject* self, PyObject* args);

// Helper function prototypes
static PyObject* encode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* table);
static PyObject* decode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* decode_table);

// Constants
extern const uint8_t base64_table[64];
extern const uint8_t base64_urlsafe_table[64];
extern const uint8_t base64_decode_table[256];

// Module definition
extern PyMethodDef Base64Methods[];
extern struct PyModuleDef base64cmodule;

// Module initialization function
PyMODINIT_FUNC PyInit_base64c(void);

#endif // BASE64C_H
poetry.lock 3706 5369cd87166957cf01698b3ba1b63fda78d30d0353cf84c995529ce6153bd074 # This file is automatically @generated by Poetry 1.8.3 and should not be changed by hand.

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "exceptiongroup"
version = "1.2.2"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
files = [
    {file = "exceptiongroup-1.2.2-py3-none-any.whl", hash = "sha256:3111b9d131c238bec2f8f516e123e14ba243563fb135d3fe885990585aa7795b"},
    {file = "exceptiongroup-1.2.2.tar.gz", hash = "sha256:47c2edf7c6738fafb49fd34290706d1a1a2f4d1c6df275526b62cbb4aa5393cc"},
]

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "iniconfig"
version = "2.0.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.7"
files = [
    {file = "iniconfig-2.0.0-py3-none-any.whl", hash = "sha256:b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374"},
    {file = "iniconfig-2.0.0.tar.gz", hash = "sha256:2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"},
]

[[package]]
name = "packaging"
version = "24.1"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
files = [
    {file = "packaging-24.1-py3-none-any.whl", hash = "sha256:5b8f2217dbdbd2f7f384c41c628544e6d52f2d0f53c6d0c3ea61aa5d1d7ff124"},
    {file = "packaging-24.1.tar.gz", hash = "sha256:026ed72c8ed3fcce5bf8950572258698927fd1dbda10a5e981cdf0ac37f4f002"},
]

[[package]]
name = "pluggy"
version = "1.5.0"
description = "plugin and hook calling mechanisms for python"
optional = false
python-versions = ">=3.8"
files = [
    {file = "pluggy-1.5.0-py3-none-any.whl", hash = "sha256:44e1ad92c8ca002de6377e165f3e0f1be63266ab4d554740532335b9d75ea669"},
    {file = "pluggy-1.5.0.tar.gz", hash = "sha256:2cffa88e94fdc978c4c574f15f9e59b7f4201d439195c3715ca9e2486f1d0cf1"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["pytest", "pytest-benchmark"]

[[package]]
name = "pytest"
version = "8.3.3"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.8"
files = [
    {file = "pytest-8.3.3-py3-none-any.whl", hash = "sha256:a6853c7375b2663155079443d2e45de913a911a11d669df02a50814944db57b2"},
    {file = "pytest-8.3.3.tar.gz", hash = "sha256:70b98107bd648308a7952b06e6ca9a50bc660be218d53c257cc1fc94fda10181"},
]

[package.dependencies]
colorama = {version = "*", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1.0.0rc8", markers = "python_version < \"3.11\""}
iniconfig = "*"
packaging = "*"
pluggy = ">=1.5,<2"
tomli = {version = ">=1", markers = "python_version < \"3.11\""}

[package.extras]
dev = ["argcomplete", "attrs (>=19.2)", "hypothesis (>=3.56)", "mock", "pygments (>=2.7.2)", "requests", "setuptools", "xmlschema"]

[[package]]
name = "tomli"
version = "2.0.2"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
files = [
    {file = "tomli-2.0.2-py3-none-any.whl", hash = "sha256:2ebe24485c53d303f690b0ec092806a085f07af5a5aa1464f3931eec36caaa38"},
    {file = "tomli-2.0.2.tar.gz", hash = "sha256:d46d457a85337051c36524bc5349dd91b1877838e2979ac5ced3e710ed8a60ed"},
]

[metadata]
lock-version = "2.0"
python-versions = "^3.8"
content-hash = "bb8f56c4e275cbd99a3082c1c912ebd4a076a5855cb3c12d0ac16c8519a6fe18"

.git/config 340 b15da96f0ddc40a0fd6fe4910ffbf1cb083885b457fc7d51f01eab382fa44bd4 [core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = https://github.com/obahamonde/base64c.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
	vscode-merge-base = origin/main

.git/objects/pack/pack-33f172b563deea7bd7148838ff92d8a536ccfcb2.pack 2840033 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
.git/objects/pack/pack-33f172b563deea7bd7148838ff92d8a536ccfcb2.idx 3284 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
.git/HEAD 21 28d25bf82af4c0e2b72f50959b2beb859e3e60b9630a5e8c603dad4ddb2b6e80 ref: refs/heads/main

.git/info/exclude 240 6671fe83b7a07c8932ee89164d1f2793b2318058eb8b98dc5c06ee0a5a3b0ec1 # git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

.git/logs/HEAD 211 65e2a74ffd83f48c21e157699e1d889eb2d152ac2b105d0bfc8c686dd66db321 0000000000000000000000000000000000000000 170b6431d0d64d4371ec9e4ada5e3e945bb0cc31 Oscar Bahamonde <oscarbahamonde@Oscars-MacBook-Air.local> 1728607278 -0500	clone: from https://github.com/obahamonde/base64c.git

.git/logs/refs/heads/main 211 65e2a74ffd83f48c21e157699e1d889eb2d152ac2b105d0bfc8c686dd66db321 0000000000000000000000000000000000000000 170b6431d0d64d4371ec9e4ada5e3e945bb0cc31 Oscar Bahamonde <oscarbahamonde@Oscars-MacBook-Air.local> 1728607278 -0500	clone: from https://github.com/obahamonde/base64c.git

.git/logs/refs/remotes/origin/HEAD 211 65e2a74ffd83f48c21e157699e1d889eb2d152ac2b105d0bfc8c686dd66db321 0000000000000000000000000000000000000000 170b6431d0d64d4371ec9e4ada5e3e945bb0cc31 Oscar Bahamonde <oscarbahamonde@Oscars-MacBook-Air.local> 1728607278 -0500	clone: from https://github.com/obahamonde/base64c.git

.git/description 73 85ab6c163d43a17ea9cf7788308bca1466f1b0a8d1cc92e26e9bf63da4062aee Unnamed repository; edit this file 'description' to name the repository.

.git/hooks/commit-msg.sample 896 1f74d5e9292979b573ebd59741d46cb93ff391acdd083d340b94370753d92437 #!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}

.git/hooks/pre-rebase.sample 4898 4febce867790052338076f4e66cc47efb14879d18097d1d61c8261859eaaa7b3 #!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END

.git/hooks/pre-commit.sample 1643 f9af7d95eb1231ecf2eba9770fedfa8d4797a12b02d7240e98d568201251244a #!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --

.git/hooks/applypatch-msg.sample 478 0223497a0b8b033aa58a3a521b8629869386cf7ab0e2f101963d328aa62193f7 #!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:

.git/hooks/fsmonitor-watchman.sample 4726 e0549964e93897b519bd8e333c037e51fff0f88ba13e086a331592bf801fa1d0 #!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}

.git/hooks/pre-receive.sample 544 a4c3d2b9c7bb3fd8d1441c31bd4ee71a595d66b44fcf49ddb310252320169989 #!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi

.git/hooks/prepare-commit-msg.sample 1492 e9ddcaa4189fddd25ed97fc8c789eca7b6ca16390b2392ae3276f0c8e1aa4619 #!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi

.git/hooks/post-update.sample 189 81765af2daef323061dcbc5e61fc16481cb74b3bac9ad8a174b186523586f6c5 #!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

.git/hooks/pre-merge-commit.sample 416 d3825a70337940ebbd0a5c072984e13245920cdf8898bd225c8d27a6dfc9cb53 #!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:

.git/hooks/pre-applypatch.sample 424 e15c5b469ea3e0a695bea6f2c82bcf8e62821074939ddd85b77e0007ff165475 #!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:

.git/hooks/pre-push.sample 1374 ecce9c7e04d3f5dd9d8ada81753dd1d549a9634b26770042b58dda00217d086a #!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

.git/hooks/update.sample 3650 8d5f2fa83e103cf08b57eaa67521df9194f45cbdbcb37da52ad586097a14d106 #!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0

.git/hooks/push-to-checkout.sample 2783 a53d0741798b287c6dd7afa64aee473f305e65d3f49463bb9d7408ec3b12bf5f #!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi

.git/refs/heads/main 41 dfb28286fb4235b9226ede001774c6d109ded8ad177e748242ba48b8b74f8c15 170b6431d0d64d4371ec9e4ada5e3e945bb0cc31

.git/refs/remotes/origin/HEAD 30 2bb6a24aa0fc6c484100f5d51a29bbad841cd2c755f5d93faa204e5dbb4eb2b4 ref: refs/remotes/origin/main

.git/index 1899 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
.git/packed-refs 112 c6962efc3112ef5edc11dcbf57e79e52e923d6d2ce1adf2f4bc2a94276a7194f # pack-refs with: peeled fully-peeled sorted 
170b6431d0d64d4371ec9e4ada5e3e945bb0cc31 refs/remotes/origin/main

assets/sample.mp3 572652 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
assets/chart.png 68230 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
assets/sample.png 1713269 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
assets/table.png 127912 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
assets/sample.jpeg 166094 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
assets/image.png 68230 651717cbddbbf74253f9495b1eb8d5930c2f5d0d1dfec760d4a804e91cf0255d [Binary]
src/.gitkeep 0 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 
src/base64c/base64c.pyi 553 f5d475a35c77d79d9f0722d4f13f1b0a17e0330d59440a5e5f108a1d50d6d4ea from typing import Union, Optional

# Standard encoding
def b64encode(s: Union[bytes, bytearray], altchars: Optional[bytes] = None) -> bytes: ...
def b64decode(s: Union[bytes, bytearray, str], altchars: Optional[bytes] = None, validate: bool = False) -> bytes: ...
def standard_b64encode(s: Union[bytes, bytearray]) -> bytes: ...
def standard_b64decode(s: Union[bytes, bytearray, str]) -> bytes: ...

# URL-safe encoding
def urlsafe_b64encode(s: Union[bytes, bytearray]) -> bytes: ...
def urlsafe_b64decode(s: Union[bytes, bytearray, str]) -> bytes: ...
src/base64c/__init__.py 426 8ee8c088e0f66d9d5959976bb53cdbdaa918aa3841f744bf1281dc45974ad68b import sys

try:
    from .base64c import b64encode, b64decode, standard_b64decode, standard_b64encode, urlsafe_b64decode, urlsafe_b64encode
except ImportError as e:
    sys.stderr.write(f"ImportError: {e}\n")
    sys.stderr.write("Make sure to build the module before importing\n")
    sys.exit(1)
    
__all__ = ['b64encode', 'b64decode', 'standard_b64decode', 'standard_b64encode', 'urlsafe_b64decode', 'urlsafe_b64encode']
