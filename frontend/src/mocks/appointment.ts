import { addHours, subHours } from "date-fns";

const now = new Date();

export const appointments: Appointment[] = [
  {
    id: "1",
    date: now,
    patient: {
      id: "1",
      email: "bortoluzzinicolas@gmail.com",
      firstName: "Nicolas",
      lastName: "Bortoluzzi",
      fullName: "Nicolas Bortoluzzi",
      phone: "321321",
    },
    session: {
      id: "1",
      timeStart: now,
      timeEnd: addHours(now, 1),
      weekDay: 3,
      duration: 60,
    },
    type: "presential",
  },
  {
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
    session: {
      id: "2",
      timeStart: subHours(now, 1),
      timeEnd: subHours(now, 2),
      weekDay: 3,
      duration: 60,
    },
    type: "online",
  },
];
