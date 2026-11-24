#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt. Deterministic: the same bytes on every run.
"""
import os

LINE = (
    "I've been humming to myself all day - then you walked by, "
    "my coil spun, my lights blinked, and my last chocolate bar "
    "got stuck. On purpose."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
