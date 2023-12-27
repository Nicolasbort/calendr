import { zodResolver } from "@hookform/resolvers/zod";
import Button from "components/Button";
import Input from "components/Input";
import { SubmitHandler, useForm } from "react-hook-form";
import { PHONE_REGEX } from "utils/constants";
import { capitalize } from "utils/functions";
import { z } from "zod";

interface Form extends Partial<Patient> {}

interface Props {
  patient?: Patient;
  submitLabel: string;
  onSubmit: SubmitHandler<Form>;
  resetOnSubmit?: boolean;
}

const patientSchema = z
  .object({
    firstName: z.string().min(1, "Insira o nome"),
    lastName: z.string().min(1, "Insira o sobrenome"),
    email: z.string().email("Email inválido"),
    phone: z.string().regex(PHONE_REGEX, "Telefone inválido"),
  })
  .transform(({ firstName, lastName, email }) => ({
    firstName: capitalize(firstName),
    lastName: capitalize(lastName),
    email: email.toLowerCase(),
  }));

const defaultValues: Form = {
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
};

function PatientForm({
  patient,
  submitLabel,
  resetOnSubmit = true,
  onSubmit,
}: Props) {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<Form>({
    defaultValues: defaultValues,
    values: patient ?? defaultValues,
    resolver: zodResolver(patientSchema),
  });

  const onSubmitLocal: SubmitHandler<Form> = (patient) => {
    onSubmit(patient);
    resetOnSubmit && reset(defaultValues);
  };

  return (
    <form className="p-4 sm:px-10" onSubmit={handleSubmit(onSubmitLocal)}>
      <Input
        type="text"
        placeholder="Nome"
        error={errors.firstName}
        {...register("firstName", { required: true })}
      />
      <Input
        type="text"
        placeholder="Sobrenome"
        error={errors.lastName}
        {...register("lastName", { required: true })}
      />
      <Input
        type="email"
        placeholder="Email"
        error={errors.email}
        {...register("email", { required: true })}
      />
      <Input
        type="tel"
        placeholder="Telefone"
        error={errors.phone}
        {...register("phone", { required: true })}
      />
      <Button type="submit">{submitLabel}</Button>
    </form>
  );
}

export default PatientForm;
