import sys

import requests
from bs4 import BeautifulSoup


class CodeFormatter:
    def __init__(self, indent: int = 2):
        self.content = []
        self.current_indent = 0
        self.indent = indent

    def open_block(self, code: str):
        self.content.append(f"{self._indent()}{code} {{")
        self.current_indent += self.indent

    def close_block(self, code: str = ""):
        self.current_indent -= self.indent
        self.content.append(f"{self._indent()}{code}}}")

    def block_comment(self, *args):
        self.content.extend(
            [
                f"{self._indent()}/**",
                f"{self._indent()} * {''.join(args)}",
                f"{self._indent()} */",
            ]
        )

    def line(self, code: str = ""):
        self.content.append(f"{self._indent()}{code}")

    def write(self, path: str = "-"):
        output = "\n".join(self.content)
        if path == "-":
            print(output)
            return

        with open(path, "w", encoding="utf-8") as _file:
            _file.write(output)

    def _indent(self):
        return self.current_indent * " "


def get_codes() -> str:
    return requests.get("https://www.iban.com/country-codes").text


def parse_codes(html: str) -> dict:
    parser = BeautifulSoup(html, "html.parser")

    table = parser.find(id="myTable").find_all("tr")

    codes = {}

    for row in table:
        cols = row.find_all("td")
        if not cols:
            continue
        codes[cols[0].text] = [cols[1].text, cols[2].text]

    return codes


def format_codes(
    codes: dict,
    class_name: str = "CountryCode",
    is_two_letters: bool = True,
    path: str = "-",
):
    formatter = CodeFormatter()

    formatter.open_block(f"export class {class_name}")

    for key in codes:
        code = codes[key][0 if is_two_letters else 1]
        formatter.block_comment(key, ": ", code)
        formatter.line(f"static readonly {code} = {class_name}.of('{code}')")
        formatter.line()

    formatter.open_block(f"static of(code: string): {class_name}")
    formatter.line(f"return new {class_name}(code)")
    formatter.close_block()
    formatter.line()
    formatter.line("private constructor(readonly code: string) {}")
    formatter.close_block()

    formatter.write(path)


if __name__ == "__main__":
    path = sys.argv[1]
    format_codes(parse_codes(get_codes()), path=path)
