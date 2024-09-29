# Base64C

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