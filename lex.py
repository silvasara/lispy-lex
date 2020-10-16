import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    token_specification = [
        ("COMMENT", r";.+?$"),
        ("LPAR",    r"\("),
        ("RPAR",    r"\)"),
        ("NUMBER",  r"[+-]?\d+(\.\d+)?"),
        ("NAME",    r"(([a-zA-Z\-\?>%!+.]+)|(?:;+.+))"),
        ("CHAR",    r"#\\\w*"),
        ("BOOL",    r"#[t|f]"),
        ("STRING",  r"\".+\""),
        ("QUOTE",   r"\'")
    ]

    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    for m in re.finditer(token_regex, code):
        kind = m.lastgroup
        value = m.group()

        if kind == "COMMENT":
            continue

        yield Token(kind, value)

    return [Token('INVALIDA', 'valor inválido')]
