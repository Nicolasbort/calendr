import { addHours, subHours } from "date-fns";

const now = new Date();

export const sessions: Session[] = [
  {
    id: "1",
    timeStart: now,
    timeEnd: addHours(now, 1),
    weekDay: 3,
    duration: 60,
    appointment: {
      id: "1",
      date: now,
      patient: {
        id: "1",
        email: "nicolas@gmail.com",
        firstName: "Nicolas",
        lastName: "Bortoluzzi",
        fullName: "Nicolas Bortoluzzi",
        phone: "321321",
      },
      type: "presential",
    },
  },
  {
    id: "2",
    timeStart: subHours(now, 1),
    timeEnd: now,
    weekDay: 3,
    duration: 60,
  },
  {
    id: "3",
    timeStart: subHours(now, 2),
    timeEnd: subHours(now, 1),
    weekDay: 3,
    duration: 60,
  },
  {
    id: "4",
    timeStart: subHours(now, 3),
    timeEnd: subHours(now, 2),
    weekDay: 3,
    duration: 60,
    appointment: {
      id: "2",
      date: now,
      patient: {
        id: "2",
        email: "bentolasena@gmail.com",
        firstName: "Bentola",
        lastName: "Sena",
        fullName: "Bentola Sena",
        phone: "321321",
      },
      type: "online",
    },
  },
];
