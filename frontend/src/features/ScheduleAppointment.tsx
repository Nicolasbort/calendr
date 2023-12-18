import { SubmitHandler, useForm } from "react-hook-form";

interface Form {
  date: Date;
  sessionId: string;
  patientId: string;
  type: "presential" | "online";
}

function ScheduleAppointment() {
  const { register, handleSubmit } = useForm<Form>();
  const onSubmit: SubmitHandler<Form> = (data) => console.log(data);

  const inputClassNames =
    "shadow appearance-none border border-gray-300 rounded-lg w-full p-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-3";

  return (
    <div className="bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg max-w-[700px]">
      <div className="py-2 border-b border-gray-300 pb-6">
        <p className="text-lg font-semibold">Agendar consulta</p>
      </div>
      <div>
        <form className="p-8 sm:px-16" onSubmit={handleSubmit(onSubmit)}>
          <input
            className={inputClassNames}
            type="date"
            placeholder="Data"
            {...register("date", { required: true })}
          />
          <select
            className={inputClassNames}
            {...register("sessionId", { required: true })}
          >
            <option selected>Selecione uma sessão</option>
            <option value="DE">Germany</option>
          </select>
          <select
            className={inputClassNames}
            {...register("patientId", { required: true })}
          >
            <option selected>Selecione um paciente</option>
            <option value="DE">Germany</option>
          </select>
          <select
            className={inputClassNames}
            {...register("type", { required: true })}
          >
            <option selected>Selecione uma modalidade</option>
            <option value="online">Online</option>
            <option value="presential">Presencial</option>
          </select>
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg w-full mt-3"
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
