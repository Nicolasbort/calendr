import { addHours, format, subHours } from "date-fns";

const now = new Date();
const oneHourLater = addHours(now, 1);
const oneHourAgo = subHours(now, 1);
const twoHourAgo = subHours(now, 2);
const threeHourAgo = subHours(now, 3);

export const sessions: Session[] = [
  {
    id: "1",
    label: `${format(now, "HH:mm")} - ${format(oneHourLater, "HH:mm")}`,
    timeStart: now,
    timeEnd: oneHourLater,
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
    label: `${format(oneHourAgo, "HH:mm")} - ${format(now, "HH:mm")}`,
    timeStart: oneHourAgo,
    timeEnd: now,
    weekDay: 3,
    duration: 60,
  },
  {
    id: "3",
    label: `${format(twoHourAgo, "HH:mm")} - ${format(oneHourAgo, "HH:mm")}`,
    timeStart: twoHourAgo,
    timeEnd: oneHourAgo,
    weekDay: 3,
    duration: 60,
  },
  {
    id: "4",
    label: `${format(threeHourAgo, "HH:mm")} - ${format(twoHourAgo, "HH:mm")}`,
    timeStart: threeHourAgo,
    timeEnd: twoHourAgo,
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
