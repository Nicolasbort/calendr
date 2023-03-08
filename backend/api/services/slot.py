def group_by_weekday(slots: list[dict]) -> dict:
    data = {}

    for slot in slots:
        if slot["week_day"] in data:
            data[slot["week_day"]].append(slot)
        else:
            data[slot["week_day"]] = [slot]

    return data
