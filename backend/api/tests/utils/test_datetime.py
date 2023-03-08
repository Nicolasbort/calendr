from datetime import datetime

import pytest
from api.utils.datetime import diff


@pytest.mark.django_db
class TestDatetimeUtil:
    @staticmethod
    @pytest.mark.parametrize(
        "time_start, time_end, expected",
        [
            ("17:00:00", "17:30:00", 30),
            ("17:00:00", "16:30:00", -30),
            ("17:00:00", "17:35:00", 35),
            ("09:00:00", "10:00:00", 60),
        ],
    )
    def test_diff(time_start, time_end, expected):
        time_start = datetime.strptime(time_start, "%H:%M:%S").time()
        time_end = datetime.strptime(time_end, "%H:%M:%S").time()

        result = diff(time_start, time_end)

        assert result == expected
