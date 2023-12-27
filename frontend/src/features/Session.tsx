import classNames from "classnames";
import { FaUser, FaWifi } from "react-icons/fa";

interface Props {
  session: Session;
  onClick: () => void;
}

function Session({ session, onClick }: Props) {
  function getType() {
    const map = {
      presential: "Presencial",
      online: "Online",
    };

    return session.appointment?.type
      ? map[session.appointment.type]
      : undefined;
  }

  function getIcon() {
    const map = {
      presential: <FaUser />,
      online: <FaWifi />,
    };

    return session.appointment?.type
      ? map[session.appointment.type]
      : undefined;
  }

  const hasAppointment = session.appointment !== undefined;
  const appointment = session.appointment;
  const isPresential = appointment?.type === "presential";

  const sessionClassNames = classNames("relative rounded-lg border py-3 px-6", {
    "border-rose-600 bg-rose-100": hasAppointment && isPresential,
    "border-blue-600 bg-blue-100": hasAppointment && !isPresential,
    "cursor-pointer hover:opacity-75": !hasAppointment,
  });
  const iconClassNames = classNames({
    "text-rose-600": hasAppointment && isPresential,
    "text-blue-600": hasAppointment && !isPresential,
  });
  const leftColorClassNames = classNames(
    "absolute left-0 top-0 bottom-0 rounded-tl-lg rounded-bl-lg w-[8px]",
    {
      "bg-rose-600": hasAppointment && isPresential,
      "bg-blue-600": hasAppointment && !isPresential,
      "bg-emerald-600": !hasAppointment,
    }
  );
  const leftColClassNames = classNames("flex justify-start text-left", {
    "items-center": !hasAppointment,
    "flex-col": hasAppointment,
  });

  return (
    <div
      className={sessionClassNames}
      onClick={() => !hasAppointment && onClick()}
    >
      <div className={leftColorClassNames}></div>
      <div className="grid grid-cols-2">
        <div className={leftColClassNames}>
          <p className="font-bold text-responsive">
            {appointment?.patient.fullName}
          </p>
          <p className="font-semibold text-responsive">{session.label}</p>
        </div>
        {hasAppointment ? (
          <div className="flex gap-3 items-center justify-end">
            <span className={iconClassNames}>{getIcon()}</span>
            <span className="font-semibold text-responsive">{getType()}</span>
          </div>
        ) : (
          <div className="flex items-center justify-end py-3">
            <span className="font-semibold text-responsive">
              Horário disponível
            </span>
          </div>
        )}
      </div>
    </div>
  );
}

export default Session;
