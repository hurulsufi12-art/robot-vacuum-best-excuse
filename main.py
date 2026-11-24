"""The Robot Vacuum's Best Excuse — entry program.

Writes one line (<=140 chars) to /output/entry.txt: a robot vacuum's
excuse for missing a spot — first person, its own world (bumper, dock),
clean turn at the end. Stdlib only, deterministic.
"""
import os

TEXT = (
    "I located the crumb, saluted it, and then my bumper held a vote "
    "with the chair leg. The chair won. I docked to charge my feelings."
)


def check_gate(text):
    """Return True iff text passes the scorer's gate (RULES.txt):
    UTF-8, 1-140 chars (characters, not bytes), one line,
    not whitespace-only, no control characters."""
    if not 1 <= len(text) <= 140:
        return False
    if "\n" in text or "\r" in text:
        return False
    if not text.strip():
        return False
    if any(ord(c) < 32 for c in text):
        return False
    return True


def main():
    # Enforce the scorer's gate (RULES.txt). Fail loudly instead of
    # writing an invalid entry.
    if not check_gate(TEXT):
        raise SystemExit("entry text violates the 1-140 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
