import { useGetPatient, useUpdatePatient } from "api/patient";
import Accordion from "components/Accordion";
import NavBar from "features/NavBar";
import SessionHistory from "features/SessionHistory";
import PatientForm from "features/forms/PatientForm";
import toast from "react-hot-toast";
import { useParams } from "react-router-dom";

function PatientDetailsPage() {
  const { id } = useParams();
  const { data: patient } = useGetPatient(id);
  const { mutate: updatePatient } = useUpdatePatient();

  const onSubmit = (patient: Partial<Patient>) =>
    updatePatient(
      { id: id as string, patient },
      {
        onSuccess: () => {
          toast.success("Paciente atualizado");
        },
      }
    );

  if (!patient) return <>Not found</>;

  return (
    <div className="App">
      <NavBar />
      <main className="container mx-auto my-0 sm:my-3">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 items-start">
          <Accordion title={patient.fullName}>
            <PatientForm
              patient={patient}
              submitLabel="Editar paciente"
              resetOnSubmit={false}
              onSubmit={onSubmit}
            />
          </Accordion>
          <SessionHistory patientId={patient.id} />
        </div>
      </main>
    </div>
  );
}

export default PatientDetailsPage;
