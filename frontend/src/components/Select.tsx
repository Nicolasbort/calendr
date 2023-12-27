import classNames from "classnames";
import ErrorMessage from "components/ErrorMessage";
import React from "react";
import { FieldError } from "react-hook-form";

interface Props extends React.SelectHTMLAttributes<HTMLSelectElement> {
  children: JSX.Element | React.ReactNode;
  error?: FieldError;
}

const Select = React.forwardRef<HTMLSelectElement, Props>((props, ref) => {
  const { children, error, ...selectProps } = props;
  const selectClassNames = classNames("input", {
    "border-red-600": error !== undefined,
  });

  return (
    <div className="mb-4">
      <select {...selectProps} ref={ref} className={selectClassNames}>
        {children}
      </select>
      <ErrorMessage error={error} />
    </div>
  );
});

export default Select;
