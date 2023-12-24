import { useListSessions } from "api/session";
import { scheduleAppointmentOpenAtom, selectedSessionAtom } from "atom";
import ComponentLoader from "components/ComponentLoader";
import Session from "features/Session";
import { useSetAtom } from "jotai";
import { FaArrowLeft, FaArrowRight } from "react-icons/fa";
import SessionListSkeleton from "./skeletons/SessionListSkeleton";

interface Props {
  date?: Date;
}

function SessionList({ date }: Props) {
  const { data: sessions, isLoading } = useListSessions(date);
  const setScheduleAppointmentOpen = useSetAtom(scheduleAppointmentOpenAtom);
  const setSelectedSession = useSetAtom(selectedSessionAtom);

  const onScheduleAppointment = (sessionId: string) => {
    setSelectedSession(sessionId);
    setScheduleAppointmentOpen(true);
  };

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
        <ComponentLoader
          isLoading={isLoading}
          skeleton={<SessionListSkeleton />}
        >
          <>
            {sessions?.map((session) => (
              <Session
                key={session.id}
                session={session}
                onClick={() => onScheduleAppointment(session.id)}
              />
            ))}
          </>
        </ComponentLoader>
      </div>
    </div>
  );
}

export default SessionList;
