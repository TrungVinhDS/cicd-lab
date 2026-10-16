import re

_DTC_PATTERN = re.compile(r"^[PCB][0-3][0-9A-F]{3}$")


def is_valid_dtc(code: str) -> bool:
    return bool(_DTC_PATTERN.match(code.strip().upper()))
