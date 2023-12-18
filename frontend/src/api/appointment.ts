import { appointments } from "mocks/appointment";
import { useMutation, useQuery, useQueryClient } from "react-query";

export const useListAppointments = () => {
  return useQuery("appointments", () => appointments);
};

export const useCreateAppointment = () => {
  const queryClient = useQueryClient();

  return useMutation<unknown, unknown, Partial<Appointment>, unknown>(
    "appointments",
    (appointment) =>
      new Promise(() =>
        queryClient.setQueryData(
          "appointments",
          (oldAppointments?: Partial<Appointment>[]) => [
            ...(oldAppointments ?? []),
            {
              id: `${Math.random().toString(16).slice(2)}`,
              ...appointment,
            },
          ]
        )
      )
  );
};
