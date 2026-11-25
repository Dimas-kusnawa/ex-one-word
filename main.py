import os

# The one-word verdict on an ex: "nonrefundable".
# A purchase with no return policy: you paid in time, attention and
# years, and when it turned out faulty there was no refund counter.
# The joke lands at a glance and needs no caption: everyone who has
# had an ex knows the feeling of money already spent, gone for good.
# It beat the other candidates head to head: "recalled" is thinner
# (a defect joke with less recognition), and "unsubscribe" is an
# action you took, not a verdict on the ex itself.
WORD = "nonrefundable"


def main():
    # Sanity guard: exactly one word, no spaces, inside the 1-111 gate.
    assert WORD == WORD.strip() and " " not in WORD and 1 <= len(WORD) <= 111
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # One word only, exactly as the gate requires: 1-111 UTF-8 chars,
    # no trailing newline, nothing added around it.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
