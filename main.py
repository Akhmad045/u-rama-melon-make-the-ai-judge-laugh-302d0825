#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, written to /output/entry.txt.

The entry is a single line about office life, under 200 characters, read
aloud in one breath. It is embedded here as a constant so the program is
fully self-contained: it reads nothing from the network, the environment,
or any file it does not ship.

Usage:
    python3 main.py            # write /output/entry.txt and verify it
    python3 main.py --self-test
"""

import argparse
import os
import sys
import tempfile

JOKE = "The only thing that moves faster than a deadline in this office is the rumour that the deadline moved."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Return an error string, or None when the text is a valid entry."""
    if not text:
        return "entry is empty"
    if not text.strip():
        return "entry is whitespace-only"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 200 limit" % len(text)
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    for ch in text:
        code = ord(ch)
        if code < 32 or code == 127:
            return "entry contains a control character U+%04X" % code
    return None


def write_entry(path):
    """Write the joke to path and read it back byte-identical."""
    data = JOKE.encode("utf-8")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        back = handle.read()
    if back != data:
        raise IOError("read-back mismatch: wrote %d bytes, read %d"
                      % (len(data), len(back)))
    return len(JOKE), len(data)


def self_test():
    """Run the validator over the entry and a battery of edge cases."""
    checks = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(("PASS" if ok else "FAIL") + " " + name)

    check("entry itself is valid", validate(JOKE) is None)
    check("empty rejected", validate("") is not None)
    check("whitespace-only rejected", validate("   \t ") is not None)
    check("201 chars rejected", validate("x" * 201) is not None)
    check("200 chars accepted", validate("x" * 200) is None)
    check("1 char accepted", validate("x") is None)
    check("multi-line rejected", validate("one\ntwo") is not None)
    check("carriage return rejected", validate("one\rtwo") is not None)
    check("leading whitespace rejected", validate(" " + JOKE) is not None)
    check("trailing whitespace rejected", validate(JOKE + " ") is not None)
    check("control character rejected", validate("a\x07b") is not None)
    check("tab rejected", validate("a\tb") is not None)

    with tempfile.TemporaryDirectory() as tmp:
        probe = os.path.join(tmp, "entry.txt")
        chars, size = write_entry(probe)
        with open(probe, "rb") as handle:
            back = handle.read()
        check("write + read-back byte-identical",
              back == JOKE.encode("utf-8"))
        check("entry is %d chars / %d bytes" % (chars, size),
              chars == len(JOKE) and size == len(JOKE.encode("utf-8")))

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("self-test FAILED: %d of %d checks failed"
              % (len(failed), len(checks)), file=sys.stderr)
        return 1
    print("self-test passed: %d of %d checks" % (len(checks), len(checks)))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the office-life joke to /output/entry.txt.")
    parser.add_argument("--self-test", action="store_true",
                        help="validate the entry and run edge-case checks")
    args = parser.parse_args(argv)

    error = validate(JOKE)
    if error is not None:
        print("entry invalid: " + error, file=sys.stderr)
        return 1

    if args.self_test:
        return self_test()

    chars, size = write_entry(OUTPUT_PATH)
    print("wrote %s (%d chars, %d bytes)" % (OUTPUT_PATH, chars, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
