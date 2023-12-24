import { scheduleAppointmentOpenAtom } from "atom";
import Modal from "components/Modal";
import ActionBar from "features/ActionBar";
import CreatePatient from "features/CreatePatient";
import NavBar from "features/NavBar";
import ScheduleAppointment from "features/ScheduleAppointment";
import SessionList from "features/SessionList";
import { useAtom } from "jotai";
import "./Home.css";

function HomePage() {
  const [scheduleAppointmentOpen, setScheduleAppointmentOpen] = useAtom(
    scheduleAppointmentOpenAtom
  );

  return (
    <div className="App">
      <NavBar />
      <ActionBar />
      <main className="container mx-auto my-0 sm:my-3">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <SessionList />
          <CreatePatient />
        </div>
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

export default HomePage;
