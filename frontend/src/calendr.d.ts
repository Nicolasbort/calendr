/// <reference types="react-scripts" />

interface Entity {
  id: string;
}

interface Patient extends Entity {
  fullName: string;
  email: string;
  phone: string;
  firstName: string;
  lastName: string;
}

interface Session extends Entity {
  label: string;
  weekDay: number;
  timeStart: Date;
  timeEnd: Date;
  duration: number;
  appointment?: Appointment;
}

interface Appointment extends Entity {
  patient: Patient;
  session?: Session;
  date: Date;
  type: "online" | "presential";
  note?: string;
  link?: string;
}
