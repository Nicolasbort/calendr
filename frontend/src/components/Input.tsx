import React from "react";

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {}

const Input = React.forwardRef<any, Props>((props, ref) => {
  return (
    <input
      {...props}
      ref={ref}
      className="shadow appearance-none border border-gray-300 rounded-lg w-full p-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4"
    />
  );
});

export default Input;
