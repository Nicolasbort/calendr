import React from "react";

interface Props extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: JSX.Element | React.ReactNode;
}

function Button({ children, ...props }: Props) {
  return (
    <button
      {...props}
      className="bg-blue-500 hover:bg-blue-700 text-white text-sm sm:text-base font-bold py-2 px-4 rounded-lg w-full mt-3"
    >
      {children}
    </button>
  );
}

export default Button;
