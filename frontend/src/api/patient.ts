import { wait } from "api";
import { patients } from "mocks/patient";
import { useMutation, useQuery, useQueryClient } from "react-query";

export const useListPatients = (_name?: string) => {
  return useQuery("patients", () => wait(1000).then(() => patients));
};

export const useCreatePatient = () => {
  const queryClient = useQueryClient();

  return useMutation<unknown, unknown, Partial<Patient>, unknown>(
    "patients",
    (patient) =>
      new Promise(() =>
        queryClient.setQueryData(
          "patients",
          (oldPatients?: Partial<Patient>[]) => [
            ...(oldPatients ?? []),
            {
              id: `${Math.random().toString(16).slice(2)}`,
              ...patient,
              fullName: `${patient.firstName} ${patient.lastName}`,
            },
          ]
        )
      )
  );
};
