import { RadioGroup } from "@headlessui/react";
import { useListPatients } from "api/patient";
import { useListSessions } from "api/session";
import { selectedSessionAtom } from "atom";
import Input from "components/Input";
import Select from "components/Select";
import { format } from "date-fns";
import { useAtomValue } from "jotai";
import { SubmitHandler, useForm } from "react-hook-form";
import toast from "react-hot-toast";

interface Form {
  date: string;
  sessionId: string;
  patientId: string;
  type: "presential" | "online";
}

function ScheduleAppointment() {
  const selectSessionId = useAtomValue(selectedSessionAtom);
  const { data: sessions } = useListSessions();
  const { data: patients } = useListPatients();
  const { register, handleSubmit, watch, setValue } = useForm<Form>({
    defaultValues: {
      date: format(new Date(), "yyyy-MM-dd"),
      sessionId: selectSessionId,
      type: "online",
      patientId: undefined,
    },
  });
  const onSubmit: SubmitHandler<Form> = (data) =>
    toast.success("Mock: consulta agendada");

  const typeValue = watch("type");

  return (
    <div className="bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg max-w-[700px]">
      <div className="py-2 text-center border-b border-gray-300 pb-5">
        <p className="text-lg font-semibold">Agendar consulta</p>
      </div>
      <div>
        <form className="p-8 sm:px-16" onSubmit={handleSubmit(onSubmit)}>
          <Input
            type="date"
            placeholder="Data"
            {...register("date", { required: true })}
          />
          <Select {...register("sessionId", { required: true })}>
            <option>Selecione uma sessão</option>
            {sessions?.map((session) => (
              <option key={session.id} value={session.id}>
                {session.duration}
              </option>
            ))}
          </Select>
          <Select {...register("patientId", { required: true })}>
            <option>Selecione um paciente</option>
            {patients?.map((patient) => (
              <option key={patient.id} value={patient.id}>
                {patient.fullName}
              </option>
            ))}
          </Select>
          <RadioGroup
            onChange={(value) => setValue("type", value)}
            value={typeValue}
            className="grid grid-cols-2"
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
                      checked ? "text-indigo-900" : "text-gray-900"
                    } block font-medium`}
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
                      checked ? "text-indigo-900" : "text-gray-900"
                    } block font-medium`}
                  >
                    Presencial
                  </RadioGroup.Label>
                </div>
              )}
            </RadioGroup.Option>
          </RadioGroup>
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg w-full mt-8"
            type="submit"
          >
            Agendar sessão
          </button>
        </form>
      </div>
    </div>
  );
}

export default ScheduleAppointment;
