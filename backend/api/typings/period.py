from datetime import time
from typing import TypedDict


class Period(TypedDict):
    time_start: time
    time_end: time
