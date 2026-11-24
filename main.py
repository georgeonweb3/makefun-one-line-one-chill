#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry. Writes one line of horror to /output/entry.txt."""
import os

ENTRY = "I counted the plates after dinner: six. We are a family of five, and the sixth plate was already licked clean."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

# Deterministic: same single line on every run, no network, no randomness.
