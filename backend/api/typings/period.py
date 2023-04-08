from dataclasses import dataclass
from datetime import time


@dataclass(repr=False, eq=False, order=False)
class Period:
    time_start: time
    time_end: time
    is_scheduled: bool = False

    def __eq__(self, __value: object) -> bool:
        return (
            self.time_start == __value.time_start and self.time_end == __value.time_end
        )
