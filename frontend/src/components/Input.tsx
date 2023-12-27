import classNames from "classnames";
import ErrorMessage from "components/ErrorMessage";
import React from "react";
import { FieldError } from "react-hook-form";

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {
  error?: FieldError;
}

const Input = React.forwardRef<HTMLInputElement, Props>((props, ref) => {
  const { error, ...inputProps } = props;
  const inputClassNames = classNames("input", {
    "border-red-600": error !== undefined,
  });

  return (
    <div className="mb-4">
      <input {...inputProps} ref={ref} className={inputClassNames} />
      <ErrorMessage error={error} />
    </div>
  );
});

export default Input;
