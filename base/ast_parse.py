import ast
import re
from typing import Any


class ParseCode(ast.NodeVisitor):
    def __init__(self, path, node_path):
        self.path = path
        self.node_path = node_path

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        print(node)


if __name__ == '__main__':
    file = open("xxx/test_preview.py")
    node = ast.parse(file.read())
    print(node)
    parse = ParseCode("", "")
    parse.visit(node)
