import { useCreatePatient } from "api/patient";
import { SubmitHandler, useForm } from "react-hook-form";

interface Form extends Partial<Patient> {}

function CreatePatient() {
  const { mutateAsync: createPatient } = useCreatePatient();

  const defaultValues: Form = {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
  };

  const { register, handleSubmit } = useForm<Form>({ defaultValues });
  const onSubmit: SubmitHandler<Form> = (data) => createPatient(data);

  const inputClassNames =
    "shadow appearance-none border border-gray-300 rounded-lg w-full p-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-3";

  return (
    <div className="hidden sm:block bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg">
      <div className="py-2 border-b border-gray-300 pb-6">
        <p className="text-lg font-semibold">Novo paciente</p>
      </div>
      <div>
        <p className="text-gray-500 mt-5">
          Cadastre pacientes manualmente, caso necessário
        </p>
        <form className="p-8 sm:px-16" onSubmit={handleSubmit(onSubmit)}>
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
            Adicionar novo paciente
          </button>
        </form>
      </div>
    </div>
  );
}

export default CreatePatient;
