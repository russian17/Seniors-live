import { young } from "./young_type";

export type event = {
  date: string;
  name: string;
  surname: string;
  imageUrl: string;
  proffesion: string;
  experience: Number;
  last_worked: string;
  competences: string[];
  atendees: young[];
};
