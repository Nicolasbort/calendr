import { useCreatePatient } from "api/patient";
import Button from "components/Button";
import Input from "components/Input";
import { SubmitHandler, useForm } from "react-hook-form";
import toast from "react-hot-toast";

interface Form extends Partial<Patient> {}

function CreatePatient() {
  const { mutate: createPatient } = useCreatePatient();

  const defaultValues: Form = {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
  };

  const { register, handleSubmit, reset } = useForm<Form>({ defaultValues });
  const onSubmit: SubmitHandler<Form> = async (data) => {
    createPatient(data, {
      onSuccess: () => {
        toast.success("Paciente adicionado!");
        reset(defaultValues);
      },
    });

    console.log("created");
  };

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
          <Button type="submit">Adicionar novo paciente</Button>
        </form>
      </div>
    </div>
  );
}

export default CreatePatient;
