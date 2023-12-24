import { addDays } from "date-fns";
import CalendarCol from "features/Calendar/CalendarCol";

interface Props {
  sessions?: Session[];
}

function Calendar({ sessions }: Props) {
  const now = new Date();

  return (
    <div className="p-3">
      <div className="grid grid-cols-5 gap-4">
        <CalendarCol date={now} />
        <CalendarCol date={addDays(now, 1)} />
        <CalendarCol date={addDays(now, 2)} />
        <CalendarCol date={addDays(now, 3)} />
        <CalendarCol date={addDays(now, 4)} />
      </div>
    </div>
  );
}

export default Calendar;
