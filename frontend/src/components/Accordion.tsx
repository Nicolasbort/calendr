import React, { useState } from "react";
import { FiMinus, FiPlus } from "react-icons/fi";

interface Props {
  title: string;
  children: JSX.Element | React.ReactNode;
}

function Accordion({ title, children }: Props) {
  const [expanded, setExpanded] = useState(false);
  const toggleExpanded = () => setExpanded(!expanded);

  return (
    <div className="bg-white border-none sm:border border-gray-300 shadow-none sm:shadow p-4 rounded-lg">
      <div
        className="px-6 text-left items-center h-20 select-none flex flex-row justify-between cursor-pointer rounded"
        onClick={toggleExpanded}
      >
        <h5 className="flex-1 font-semibold text-lg">{title}</h5>
        <div className="flex-none pl-2">
          {expanded ? <FiMinus /> : <FiPlus />}
        </div>
      </div>
      <div
        className={`px-6 pt-0 overflow-hidden transition-[max-height] duration-200 ease-in ${
          expanded ? "max-h-screen" : "max-h-0"
        }`}
      >
        <div className="pb-4 text-left">{children}</div>
      </div>
    </div>
  );
}

export default Accordion;
