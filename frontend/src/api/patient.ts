import { wait } from "api";
import { useMutation, useQuery, useQueryClient } from "react-query";
import { createItem, getItem, listItems, updateItem } from "utils/crud";

const KEY = "PATIENTS";

export const useListPatients = (_name?: string) => {
  return useQuery(KEY, () => listItems<Patient>(KEY));
};

export const useGetPatient = (patientId?: string, opts = {}) =>
  useQuery(
    [KEY, patientId],
    () => {
      if (!patientId) return undefined;

      return getItem<Patient>(KEY, patientId);
    },
    opts
  );

export const useCreatePatient = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (patient: Partial<Patient>) =>
      wait(0).then(() => {
        const processedPatient = {
          ...patient,
          id: `${Math.random().toString(16).slice(2)}`,
          fullName: `${patient.firstName} ${patient.lastName}`,
        };

        return createItem<Patient>(KEY, processedPatient);
      }),
    onSuccess: () => queryClient.invalidateQueries(KEY),
  });
};

export const useUpdatePatient = () => {
  const queryClient = useQueryClient();

  return useMutation<any, any, { id: string; patient: Partial<Patient> }, any>({
    mutationFn: ({ id, patient }) =>
      wait(0).then(() => {
        const processedPatient = {
          ...patient,
          fullName: `${patient.firstName} ${patient.lastName}`,
        };

        return updateItem<Patient>(KEY, id, processedPatient);
      }),
    onSuccess: (_data, { id }, _context) =>
      queryClient.invalidateQueries([KEY, id]),
  });
};
