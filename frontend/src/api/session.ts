import { wait } from "api";
import { sessions } from "mocks/session";
import { useQuery } from "react-query";

export const useListSessions = (_date?: Date) => {
  return useQuery<Session[]>("sessions", () => {
    return wait(1000).then(() => sessions);
  });
};
