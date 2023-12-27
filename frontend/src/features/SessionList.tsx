import { useListSessions } from "api/session";
import {
  scheduleAppointmentOpenAtom,
  selectedSessionAtom,
  todayAtom,
} from "atom";
import ComponentLoader from "components/ComponentLoader";
import { format } from "date-fns";
import { ptBR } from "date-fns/locale";
import Session from "features/Session";
import { useAtomValue, useSetAtom } from "jotai";
import { FaArrowLeft, FaArrowRight } from "react-icons/fa";
import { capitalize } from "utils/functions";
import SessionListSkeleton from "./skeletons/SessionListSkeleton";

interface Props {
  date?: Date;
}

function SessionList({ date }: Props) {
  const today = useAtomValue(todayAtom);
  const { data: sessions, isLoading } = useListSessions(date);
  const setScheduleAppointmentOpen = useSetAtom(scheduleAppointmentOpenAtom);
  const setSelectedSession = useSetAtom(selectedSessionAtom);

  const onScheduleAppointment = (sessionId: string) => {
    setSelectedSession(sessionId);
    setScheduleAppointmentOpen(true);
  };

  return (
    <div>
      <div className="bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg">
        <div className="px-3">
          <div className="flex justify-between items-center pb-3 border-b border-gray-300">
            <button>
              <FaArrowLeft />
            </button>
            <div>
              <p className="font-semibold text-xl">Hoje</p>
              <p className="text-sm text-gray-600">
                {capitalize(
                  format(today, "EEEE',' d 'de' MMMM", { locale: ptBR })
                )}
              </p>
            </div>
            <button>
              <FaArrowRight />
            </button>
          </div>
          <ComponentLoader
            isLoading={isLoading}
            skeleton={<SessionListSkeleton />}
          >
            <div className="py-5 flex flex-col gap-3">
              {sessions?.map((session) => (
                <Session
                  key={session.id}
                  session={session}
                  onClick={() => onScheduleAppointment(session.id)}
                />
              ))}
            </div>
          </ComponentLoader>
        </div>
      </div>
    </div>
  );
}

export default SessionList;
