import { wait } from "api";
import { sessions } from "mocks/session";
import { useQuery } from "react-query";

export const useListSessions = () => {
  return useQuery<Session[]>("sessions", () => {
    return wait(3000).then(() => sessions);
  });
  // return useQuery("sessions", () => sessions);
};
