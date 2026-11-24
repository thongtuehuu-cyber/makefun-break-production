import os

LINE = "I rolled back the deploy and the rollback. Both are down now. I am the incident."

MIN_LEN = 1
MAX_LEN = 200


def validate_line(line):
    """Gate: UTF-8, 1-200 chars, not only whitespace, one line, no
    leading/trailing whitespace."""
    assert MIN_LEN <= len(line) <= MAX_LEN, "line must be 1-200 characters"
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    return line


def write_entry(line, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify the write round-trips byte-identically before reporting success.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "entry.txt does not match the winning line"
    return path


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(line, out_dir)


if __name__ == "__main__":
    main()
