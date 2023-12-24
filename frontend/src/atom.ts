import { atom } from "jotai";

export const scheduleAppointmentOpenAtom = atom(false);
export const searchTextAtom = atom<string>("");
export const selectedSessionAtom = atom<string | undefined>("");
