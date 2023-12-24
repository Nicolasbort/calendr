import { scheduleAppointmentOpenAtom } from "atom";
import Modal from "components/Modal";
import NavBar from "features/NavBar";
import PatientList from "features/PatientList";
import ScheduleAppointment from "features/ScheduleAppointment";
import { useAtom } from "jotai";
import "./Home.css";

function SearchPage() {
  const [scheduleAppointmentOpen, setScheduleAppointmentOpen] = useAtom(
    scheduleAppointmentOpenAtom
  );

  return (
    <div className="App">
      <NavBar />
      <main className="container mx-auto my-0 sm:my-3">
        <PatientList />
        <Modal
          isOpen={scheduleAppointmentOpen}
          onClose={() => setScheduleAppointmentOpen(false)}
        >
          <ScheduleAppointment />
        </Modal>
      </main>
    </div>
  );
}

export default SearchPage;
