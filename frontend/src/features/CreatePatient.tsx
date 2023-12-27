import { useCreatePatient } from "api/patient";
import toast from "react-hot-toast";
import PatientForm from "./forms/PatientForm";

function CreatePatient() {
  const { mutate: createPatient } = useCreatePatient();

  const onSubmit = (patient: Partial<Patient>) =>
    createPatient(patient, {
      onSuccess: () => {
        toast.success("Paciente adicionado!");
      },
    });

  return (
    <div>
      <div className="hidden sm:block bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg">
        <div className="py-2 border-b border-gray-300 pb-6">
          <p className="text-lg font-semibold">Novo paciente</p>
        </div>
        <div>
          <p className="text-gray-500 mt-5">
            Cadastre pacientes manualmente, caso necessário
          </p>
          <PatientForm submitLabel="Adicionar paciente" onSubmit={onSubmit} />
        </div>
      </div>
    </div>
  );
}

export default CreatePatient;
