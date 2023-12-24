import { useGetPatient, useUpdatePatient } from "api/patient";
import Accordion from "components/Accordion";
import Button from "components/Button";
import Input from "components/Input";
import NavBar from "features/NavBar";
import SessionHistory from "features/SessionHistory";
import { SubmitHandler, useForm } from "react-hook-form";
import toast from "react-hot-toast";
import { useParams } from "react-router-dom";

interface Form extends Partial<Patient> {}

function PatientDetailsPage() {
  const { id } = useParams();
  const { data: patient } = useGetPatient(id);
  const { mutate: updatePatient } = useUpdatePatient();
  const { register, handleSubmit } = useForm<Form>({ values: patient });

  const onSubmit: SubmitHandler<Form> = (patient) => {
    updatePatient(patient, {
      onSuccess: () => {
        toast.success("Paciente atualizado");
      },
    });
  };

  if (!patient) return <>Not found</>;

  return (
    <div className="App">
      <NavBar />
      <main className="container mx-auto my-0 sm:my-3">
        <div className="grid grid-cols-1 sm:grid-cols-2 items-start">
          <Accordion title={patient.fullName}>
            <form
              className="bg-white rounded px-3 py-6"
              onSubmit={handleSubmit(onSubmit)}
            >
              <Input
                type="text"
                placeholder="Nome"
                {...register("firstName", { required: true })}
              />
              <Input
                type="text"
                placeholder="Sobrenome"
                {...register("lastName", { required: true })}
              />
              <Input
                type="email"
                placeholder="Email"
                {...register("email", { required: true })}
              />
              <Input
                type="tel"
                placeholder="Telefone"
                {...register("phone", { required: true })}
              />
              <Button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg w-full mt-3"
                type="submit"
              >
                Editar paciente
              </Button>
            </form>
          </Accordion>
          <SessionHistory patientId={patient.id} />
        </div>
      </main>
    </div>
  );
}

export default PatientDetailsPage;
