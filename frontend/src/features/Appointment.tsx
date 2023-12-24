import classNames from "classnames";
import { format } from "date-fns";
import { FaUser } from "react-icons/fa";

interface Props {
  appointment: Appointment;
}

function Appointment({ appointment }: Props) {
  function getType() {
    const map = {
      presential: "Presencial",
      online: "Online",
    };

    return map[appointment.type];
  }

  const isPresential = appointment.type === "presential";
  const appointmentClassNames = classNames(
    "relative rounded-lg border py-3 px-6",
    {
      "border-red-600 bg-red-100": isPresential,
      "border-blue-600 bg-blue-100": !isPresential,
    }
  );
  const iconClassNames = classNames({
    "text-red-600": isPresential,
    "text-blue-600": !isPresential,
  });
  const leftColorClassNames = classNames(
    "absolute left-0 top-0 bottom-0 rounded-tl-lg rounded-bl-lg w-[8px]",
    {
      "bg-red-600": isPresential,
      "bg-blue-600": !isPresential,
    }
  );

  return (
    <div className={appointmentClassNames}>
      <div className={leftColorClassNames}></div>
      <div className="grid grid-cols-2">
        <div className="flex flex-col justify-start text-left">
          <p className="font-bold text-responsive">
            {appointment.patient.fullName}
          </p>
          {appointment.session && (
            <p className="font-semibold text-responsive">
              {format(appointment.session.timeStart, "HH:mm")} -{" "}
              {format(appointment.session.timeEnd, "HH:mm")}
            </p>
          )}
        </div>
        <div className="flex gap-3 items-center justify-end">
          <FaUser className={iconClassNames} />
          <span className="font-semibold text-responsive">{getType()}</span>
        </div>
      </div>
    </div>
  );
}

export default Appointment;
