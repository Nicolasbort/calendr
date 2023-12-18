import { useListSessions } from "api/session";
import { scheduleAppointmentOpenAtom } from "atom";
import Session from "components/Session";
import { useSetAtom } from "jotai";
import { FaArrowLeft, FaArrowRight } from "react-icons/fa";
import SessionListSkeleton from "./skeletons/SessionListSkeleton";

function SessionList() {
  const { data: sessions, isLoading } = useListSessions();
  const setScheduleAppointmentOpen = useSetAtom(scheduleAppointmentOpenAtom);

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
        {isLoading ? (
          <SessionListSkeleton />
        ) : (
          sessions?.map((session) => (
            <Session
              key={session.id}
              session={session}
              onClick={() => setScheduleAppointmentOpen(true)}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default SessionList;
