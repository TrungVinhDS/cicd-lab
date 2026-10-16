import sys

from app.dtc import is_valid_dtc

if __name__ == "__main__":
    for code in sys.argv[1:]:
        print(f"{code}: {'valid' if is_valid_dtc(code) else 'invalid'}")
