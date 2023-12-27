import { RadioGroup } from "@headlessui/react";
import { zodResolver } from "@hookform/resolvers/zod";
import { useListPatients } from "api/patient";
import { useListSessions } from "api/session";
import { selectedSessionAtom } from "atom";
import Button from "components/Button";
import Input from "components/Input";
import Select from "components/Select";
import { format } from "date-fns";
import { useAtom } from "jotai";
import { useEffect } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";

interface Form {
  date: string;
  sessionId: string;
  patientId: string;
  type: "presential" | "online";
}

interface Props {
  onSubmit: SubmitHandler<Form>;
  resetOnSubmit?: boolean;
}

const appointmentScheam = z.object({
  date: z.string().min(1, "Insira uma data"),
  patientId: z.string().min(1, "Selecione um paciente"),
  sessionId: z.string().min(1, "Selecione uma sessão"),
  type: z.string(),
});

const defaultValues: Form = {
  date: format(new Date(), "yyyy-MM-dd"),
  sessionId: "",
  patientId: "",
  type: "online",
};

function AppointmentForm({ resetOnSubmit = true, onSubmit }: Props) {
  const [selectSessionId, setSelectedSessionId] = useAtom(selectedSessionAtom);
  const { data: sessions } = useListSessions();
  const { data: patients } = useListPatients();
  const {
    register,
    handleSubmit,
    reset,
    watch,
    setValue,
    formState: { errors },
  } = useForm<Form>({
    defaultValues: defaultValues,
    values: {
      ...defaultValues,
      sessionId: selectSessionId,
    },
    resolver: zodResolver(appointmentScheam),
  });

  const onSubmitLocal: SubmitHandler<Form> = (appointment) => {
    onSubmit(appointment);
    resetOnSubmit && reset(defaultValues);
  };

  const typeValue = watch("type");

  useEffect(() => {
    return () => setSelectedSessionId("");
  }, []);

  return (
    <form className="p-4 sm:px-10" onSubmit={handleSubmit(onSubmitLocal)}>
      <Input
        type="date"
        placeholder="Data"
        error={errors.date}
        {...register("date", { required: true })}
      />
      <Select
        error={errors.sessionId}
        {...register("sessionId", { required: true })}
      >
        <option disabled value="">
          Selecione uma sessão
        </option>
        {sessions?.map((session) => (
          <option key={session.id} value={session.id}>
            {session.label}
          </option>
        ))}
      </Select>
      <Select
        error={errors.patientId}
        {...register("patientId", { required: true })}
      >
        <option disabled value="">
          Selecione um paciente
        </option>
        {patients?.map((patient) => (
          <option key={patient.id} value={patient.id}>
            {patient.fullName}
          </option>
        ))}
      </Select>
      <RadioGroup
        onChange={(value) => setValue("type", value)}
        value={typeValue}
        className="grid grid-cols-2 mb-3"
      >
        <RadioGroup.Option
          value="online"
          className={({ checked }) => `
            ${checked ? "border-blue-300 bg-sky-100" : "border-gray-300"}
            relative flex border py-2 cursor-pointer rounded-l-lg justify-center shadow
          `}
        >
          {({ checked }) => (
            <div className="flex flex-col items-center">
              <RadioGroup.Label
                as="span"
                className={`${
                  checked ? "text-blue-800" : "text-gray-600"
                } block font-medium text-xs sm:text-base`}
              >
                Online
              </RadioGroup.Label>
            </div>
          )}
        </RadioGroup.Option>
        <RadioGroup.Option
          value="presential"
          className={({ checked }) => `
            ${checked ? "border-blue-300 bg-sky-100" : "border-gray-300"}
            relative flex border py-2 cursor-pointer rounded-r-lg justify-center shadow
          `}
        >
          {({ checked }) => (
            <div className="flex flex-col">
              <RadioGroup.Label
                as="span"
                className={`${
                  checked ? "text-blue-800" : "text-gray-600"
                } block font-medium text-xs sm:text-base`}
              >
                Presencial
              </RadioGroup.Label>
            </div>
          )}
        </RadioGroup.Option>
      </RadioGroup>
      <Button>Agendar sessão</Button>
    </form>
  );
}

export default AppointmentForm;
