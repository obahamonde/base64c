import sys

try:
    from .base64c import b64encode, b64decode, standard_b64decode, standard_b64encode, urlsafe_b64decode, urlsafe_b64encode
except ImportError as e:
    sys.stderr.write(f"ImportError: {e}\n")
    sys.stderr.write("Make sure to build the module before importing\n")
    sys.exit(1)
    
__all__ = ['b64encode', 'b64decode', 'standard_b64decode', 'standard_b64encode', 'urlsafe_b64decode', 'urlsafe_b64encode']