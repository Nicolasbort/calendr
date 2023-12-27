import MailBox from "mailbox.png";
import SessionList from "./SessionList";

interface Props {
  patientId: string;
}

function SessionHistory({ patientId }: Props) {
  return <SessionList />;

  return (
    <div className="p-3 flex flex-col justify-center items-center gap-5">
      <p className="text-xl font-semibold">Histórico de sessões</p>
      <img className="w-1/2 sm:w-1/3" src={MailBox} alt="Mail box" />
      <div>
        <p className="font-semibold text-lg">Nada por aqui</p>
        <p className="text-gray-500">
          O paciente não possui sessão por enquanto
        </p>
      </div>
    </div>
  );
}

export default SessionHistory;
