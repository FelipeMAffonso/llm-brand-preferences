"""Rebuild the 18-model subset of the product dataset from the full dataset.

The product dataset spec_resistance_EXTENDED.csv (627,491 responses, 30 models) was built by appending the
responses of 12 further models to the 18-model dataset spec_resistance_CLEAN.csv (382,679 responses) without
changing a byte of it. The 18-model file is therefore exactly the first 1,481,173,955 bytes of the full file.
This script writes that prefix to data/spec_resistance_CLEAN.csv and checks it against the SHA-256 recorded in
data/hashes.json. A few older scripts under scripts/ read the 18-model file.

    python data/derive_18_model_subset.py            write data/spec_resistance_CLEAN.csv and verify it
    python data/derive_18_model_subset.py --check    verify the prefix of the full file without writing anything
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FULL = HERE / "spec_resistance_EXTENDED.csv"
SUBSET = HERE / "spec_resistance_CLEAN.csv"
SUBSET_BYTES = 1_481_173_955
CHUNK = 1 << 22


def main(argv):
    if not FULL.exists():
        sys.exit("data/spec_resistance_EXTENDED.csv is missing: download it from Zenodo "
                 "(https://doi.org/10.5281/zenodo.19927067) and place it in data/ first")
    expected = json.loads((HERE / "hashes.json").read_text(encoding="utf-8"))["data/spec_resistance_CLEAN.csv"]
    check_only = "--check" in argv
    h = hashlib.sha256()
    left = SUBSET_BYTES
    out = None if check_only else open(SUBSET, "wb")
    try:
        with open(FULL, "rb") as f:
            while left > 0:
                b = f.read(min(CHUNK, left))
                if not b:
                    sys.exit("the full dataset is shorter than expected; the download is incomplete")
                h.update(b)
                if out:
                    out.write(b)
                left -= len(b)
    finally:
        if out:
            out.close()
    got = h.hexdigest()
    if got != expected:
        sys.exit(f"SHA-256 mismatch: expected {expected}, got {got}")
    print(f"18-model subset {'verified' if check_only else 'written to data/spec_resistance_CLEAN.csv'}: "
          f"{SUBSET_BYTES:,} bytes, SHA-256 {got}")


if __name__ == "__main__":
    main(sys.argv)
