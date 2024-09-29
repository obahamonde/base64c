# base64c

A faster base64 encoding/decoding library for Python, implemented in C with SSSE3 optimizations.

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



