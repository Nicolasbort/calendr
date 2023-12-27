import { FieldError } from "react-hook-form";

interface Props {
  error?: FieldError;
}

function ErrorMessage({ error }: Props) {
  if (!error) return null;

  return (
    <p className="pl-1 pt-0 sm:pt-1 text-start text-red-500 text-xs">
      {error.message}
    </p>
  );
}

export default ErrorMessage;
