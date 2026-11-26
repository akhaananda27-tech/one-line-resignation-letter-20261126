# SPDX-License-Identifier: MIT
"""Print the one-line resignation letter for make.fun bounty
u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947."""

from pathlib import Path

line = (Path(__file__).parent / "line.txt").read_text(encoding="utf-8").strip()
print(line)  # the entry is exactly this one line, nothing else
