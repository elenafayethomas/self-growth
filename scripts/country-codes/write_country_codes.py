import re
import sys

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

EXCEPTIONS = {
    "Iran (Islamic Republic of)": "IRAN",
    "Korea (the Democratic People's Republic of)": "NORTH_KOREA",
    "Korea (the Republic of)": "SOUTH_KOREA",
    "Taiwan (Province of China)": "TAIWAN",
    "United Kingdom of Great Britain and Northern Ireland (the)": "UNITED_KINGDOM",
    "United States of America (the)": "UNITED_STATES",
}


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

    def format_country_name(name: str) -> str:
        if name in EXCEPTIONS:
            return EXCEPTIONS[name]

        _name = unidecode(name.lower())
        matches = re.findall(
            "'|\,|\-|\.|\([a-zA-Z0-9_,'-. ]+\)|\[[a-zA-Z0-9_,'-. ]+\]", _name
        )

        if len(matches) > 0:
            matches.reverse()  # performs reverse on the original list. Has no return value
            for match in matches:
                _name = "{0} {1}".format(
                    re.sub("[\[\]\(\),'-.]", "", match), _name.replace(match, "")
                )

        return "_".join(_name.upper().split())

    for key in codes:
        code = codes[key][0 if is_two_letters else 1]
        formatter.block_comment(key, ": ", code)
        formatter.line(
            f"static readonly {format_country_name(key)} = {class_name}.of('{code}')"
        )
        formatter.line()

    formatter.open_block(f"static of(code: string): {class_name}")
    formatter.line(f"return new {class_name}(code)")
    formatter.close_block()
    formatter.line()
    formatter.line("private constructor(readonly code: string) {}")
    formatter.close_block()

    formatter.write(path)


if __name__ == "__main__":
    path = "-"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    format_codes(parse_codes(get_codes()), path=path)
