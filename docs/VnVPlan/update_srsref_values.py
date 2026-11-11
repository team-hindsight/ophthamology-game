import re
from pathlib import Path

file = Path("VnVPlan.tex")
text = file.read_text(encoding="utf-8")

def increment(match):
    number = int(match.group(2))
    # Edit this condition to change all numbers above the new FR requirement you are introducing. For example, if I make a new FR15 in SRS, then VnVPlan needs to be updated from FR15 up
    if number >= 29:
        number += 1
    return f"{match.group(1)}{number}{match.group(3)}"

updated = re.sub(
    r'(\\srsfrref\{[^}]+\}\{)(\d+)(\})',
    increment,
    text
)

file.write_text(updated, encoding="utf-8")