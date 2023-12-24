import { IoIosArrowForward } from "react-icons/io";

interface Props {
  patient: Patient;
}

function Patient({ patient }: Props) {
  return (
    <div className="rounded-lg p-3 border bg-white cursor-pointer">
      <div className="flex justify-between items-center text-left">
        <p className="font-bold text-responsive">{patient.fullName}</p>
        <IoIosArrowForward className="w-7 h-7" />
      </div>
    </div>
  );
}

export default Patient;
