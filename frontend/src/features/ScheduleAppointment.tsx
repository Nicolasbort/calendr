import { SubmitHandler } from "react-hook-form";
import toast from "react-hot-toast";
import AppointmentForm from "./forms/AppointmentForm";

interface Form {
  date: string;
  sessionId: string;
  patientId: string;
  type: "presential" | "online";
}

function ScheduleAppointment() {
  const onSubmit: SubmitHandler<Form> = (data) =>
    toast.success(`Consulta agendada: ${JSON.stringify(data, null, 2)}`, {
      duration: 5000,
    });

  return (
    <div>
      <div className="text-center">
        <p className="text-lg font-semibold">Agendar consulta</p>
      </div>
      <hr className="m-4" />
      <div>
        <AppointmentForm onSubmit={onSubmit} />
      </div>
    </div>
  );
}

export default ScheduleAppointment;
