"""Entry for make.fun: Charm the Commuter: Forecast a City That Isn't.

Umbrellwick expects polite spoon rain on the morning commute.
"""
import os

LINE = "Tomorrow in Umbrellwick: sunny with a 90% chance of spoons raining politely; commuters are advised to stir, not run."
MAX_CHARS = 140


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
