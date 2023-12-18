import React from "react";

interface Props {
  icon: JSX.Element;
  label: string;
  onClick: React.MouseEventHandler<HTMLButtonElement>;
}

function Action({ icon, label, onClick }: Props) {
  return (
    <div className="flex justify-center items-center">
      <button
        className="flex flex-col gap-3 items-center justify-center rounded-lg aspect-square sm:aspect-auto hover:opacity-75 p-1 sm:p-3 border border-gray-300 bg-white w-4/5 sm:w-full"
        onClick={onClick}
      >
        <div className="text-blue-600">{icon}</div>
        <p className="text-responsive">{label}</p>
      </button>
    </div>
  );
}

export default Action;
