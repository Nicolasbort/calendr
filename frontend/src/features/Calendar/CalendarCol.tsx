import CalendarTime from "components/CalendarTime";
import { format } from "date-fns";

interface Props {
  date: Date;
  sessions?: Session[];
}

function CalendarCol({ date, sessions }: Props) {
  return (
    <div className="flex flex-col gap-3">
      <div>
        <p className="font-bold">{format(date, "d")}</p>
      </div>
      <CalendarTime time={format(date, "HH:mm")} />
      <CalendarTime time="10:00" disabled />
      <CalendarTime time="9:00" />
      <CalendarTime time="9:00" />
      <CalendarTime time="9:00" />
    </div>
  );
}

export default CalendarCol;
