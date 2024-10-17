from __future__ import annotations
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
