import { atom } from "jotai";

export const scheduleAppointmentOpenAtom = atom(false);
export const searchTextAtom = atom<string>("");
export const selectedSessionAtom = atom<string>("");
export const todayAtom = atom<Date>(new Date());
