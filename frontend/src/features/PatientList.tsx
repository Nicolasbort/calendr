import { useListPatients } from "api/patient";
import { searchTextAtom } from "atom";
import ComponentLoader from "components/ComponentLoader";
import Patient from "components/Patient";
import { useAtomValue } from "jotai";
import PatientListSkeleton from "./skeletons/PatientListSkeleton";

function PatientList() {
  const patientName = useAtomValue(searchTextAtom);

  const { data: patients, isLoading } = useListPatients(patientName);

  return (
    <div className="border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg bg-gray-50">
      <p className="font-semibold text-2xl text-center mb-4">Pacientes</p>
      <div className="flex flex-col gap-3 px-3">
        <ComponentLoader
          isLoading={isLoading}
          skeleton={<PatientListSkeleton />}
        >
          <>
            {patients?.map((patient) => (
              <Patient key={patient.id} patient={patient} />
            ))}
          </>
        </ComponentLoader>
      </div>
    </div>
  );
}

export default PatientList;
