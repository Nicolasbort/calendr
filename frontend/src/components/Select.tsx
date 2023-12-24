import React from "react";

interface Props extends React.SelectHTMLAttributes<HTMLSelectElement> {
  children: JSX.Element | React.ReactNode;
}

const Select = React.forwardRef<any, Props>(({ children, ...props }, ref) => {
  return (
    <select
      {...props}
      ref={ref}
      className="shadow appearance-none border border-gray-300 rounded-lg w-full p-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4"
    >
      {children}
    </select>
  );
});

export default Select;
