import Calendar from "features/Calendar";
import NavBar from "features/NavBar";
import { useParams } from "react-router-dom";
import "./Home.css";

function CalendarPage() {
  const { username } = useParams();

  return (
    <div className="App">
      <NavBar />
      <main className="container mx-auto my-0 sm:my-3">
        <Calendar />
      </main>
    </div>
  );
}

export default CalendarPage;
