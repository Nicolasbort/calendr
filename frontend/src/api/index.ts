import axios from "axios";

const JWT_TOKEN = localStorage && localStorage.getItem("auth:token");

export const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  timeout: 15000,
  headers: {
    "Content-Type": "application/json; charset=utf-8",
    Authorization: JWT_TOKEN ? `Bearer ${JWT_TOKEN}` : undefined,
  },
});

// Temporary function to simulate API loading
export async function wait(duration: number = 0): Promise<any> {
  return new Promise((resolver) => setTimeout(resolver, duration));
}

export const numberFormat = Intl.NumberFormat(undefined, {
  style: "currency",
  currency: "BRL",
  maximumSignificantDigits: 1,
  minimumSignificantDigits: 1,
  minimumFractionDigits: 1,
  maximumFractionDigits: 1,
});

export const formatCurrency = (value: number): string => {
  const formatedValue = value / 100;

  return `R$ ${formatedValue.toFixed(2)}`;
};
