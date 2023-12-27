import { scheduleAppointmentOpenAtom } from "atom";
import Action from "components/Action";
import { useSetAtom } from "jotai";
import React from "react";
import toast from "react-hot-toast";
import { FaCalendar, FaHeart, FaUserPlus } from "react-icons/fa";

function ActionBar() {
  const setScheduleAppointmentOpen = useSetAtom(scheduleAppointmentOpenAtom);

  const onScheduleAppointment = (e: React.MouseEvent) => {
    setScheduleAppointmentOpen(true);
  };

  const onNewPatient = (e: React.MouseEvent) => toast.error("Não implementado");

  const onShareAgenda = (e: React.MouseEvent) =>
    toast.error("Não implementado");

  return (
    <header className="bg-gray-50">
      <div className="max-w-screen-xl grid grid-cols-3 gap-0 xl:gap-10 justify-around mx-auto py-4">
        <Action
          icon={<FaHeart />}
          label="Agendar Consulta"
          onClick={onScheduleAppointment}
        />
        <Action
          icon={<FaUserPlus />}
          label="Novo Paciente"
          onClick={onNewPatient}
        />
        <Action
          icon={<FaCalendar />}
          label="Compartilhar Agenda"
          onClick={onShareAgenda}
        />
      </div>
    </header>
  );
}

export default ActionBar;
