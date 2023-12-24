import { IoIosArrowForward } from "react-icons/io";

interface Props {
  patient: Patient;
  onClick: (patientId: string) => void;
}

function Patient({ patient, onClick }: Props) {
  return (
    <div
      className="rounded-lg p-3 border bg-white cursor-pointer"
      onClick={() => onClick(patient.id)}
    >
      <div className="flex justify-between items-center text-left">
        <p className="font-bold text-responsive">{patient.fullName}</p>
        <IoIosArrowForward className="w-7 h-7" />
      </div>
    </div>
  );
}

export default Patient;
