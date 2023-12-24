import { useGetPatient } from "api/patient";
import Accordion from "components/Accordion";
import NavBar from "features/NavBar";
import SessionHistory from "features/SessionHistory";
import { SubmitHandler, useForm } from "react-hook-form";
import { useParams } from "react-router-dom";

interface Form extends Partial<Patient> {}

function PatientDetailsPage() {
  const { id } = useParams();
  const { data: patient } = useGetPatient(id, { enabled: id !== undefined });
  const { register, handleSubmit } = useForm<Form>({ defaultValues: patient });

  const onSubmit: SubmitHandler<Form> = (data) => console.log(data);

  if (!patient) return <>Not found</>;

  const inputClassNames =
    "shadow border appearance-none rounded-lg w-full p-3 text-gray-700 leading-tight outline-none focus:shadow-outline mb-4";

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
              <input
                className={inputClassNames}
                type="text"
                placeholder="Nome"
                {...register("firstName", { required: true })}
              />
              <input
                className={inputClassNames}
                type="text"
                placeholder="Sobrenome"
                {...register("lastName", { required: true })}
              />
              <input
                className={inputClassNames}
                type="email"
                placeholder="Email"
                {...register("email", { required: true })}
              />
              <input
                className={inputClassNames}
                type="tel"
                placeholder="Telefone"
                {...register("phone", { required: true })}
              />
              <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg w-full mt-3"
                type="submit"
              >
                Editar paciente
              </button>
            </form>
          </Accordion>
          <SessionHistory patientId={patient.id} />
        </div>
      </main>
    </div>
  );
}

export default PatientDetailsPage;
