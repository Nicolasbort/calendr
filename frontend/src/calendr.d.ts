/// <reference types="react-scripts" />

interface Patient {
  id: string;
  fullName: string;
  email: string;
  phone: string;
  firstName: string;
  lastName: string;
}

interface Session {
  id: string;
  weekDay: number;
  timeStart: Date;
  timeEnd: Date;
  duration: number;
  appointment?: Appointment;
}

interface Appointment {
  id: string;
  patient: Patient;
  session?: Session;
  date: Date;
  type: "online" | "presential";
  note?: string;
  link?: string;
}
