import { useListAppointments } from "api/appointment";
import Appointment from "components/Appointment";
import { FaArrowLeft, FaArrowRight } from "react-icons/fa";

function AppointmentList() {
  const { data: appointments } = useListAppointments();

  return (
    <div className="bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg">
      <div className="flex flex-col gap-3 px-3">
        <div className="flex justify-between items-center pb-3 border-b border-gray-300">
          <button>
            <FaArrowLeft />
          </button>
          <div>
            <p className="font-semibold text-xl">Hoje</p>
            <p className="text-sm text-gray-600">Sábado, 1 de abril</p>
          </div>
          <button>
            <FaArrowRight />
          </button>
        </div>
        {appointments?.map((appointment) => (
          <Appointment key={appointment.id} appointment={appointment} />
        ))}
      </div>
    </div>
  );
}

export default AppointmentList;
