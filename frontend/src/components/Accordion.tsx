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
    <div
      className="my-2 sm:my-4 md:my-6 shadow cursor-pointer bg-white"
      onClick={toggleExpanded}
    >
      <div className="px-6 text-left items-center h-20 select-none flex justify-between flex-row">
        <h5 className="flex-1 font-semibold text-lg">{title}</h5>
        <div className="flex-none pl-2">
          {expanded ? <FiMinus /> : <FiPlus />}
        </div>
      </div>
      <div
        className={`px-6 pt-0 overflow-hidden transition-[max-height] duration-250 ease-in ${
          expanded ? "max-h-screen" : "max-h-0"
        }`}
      >
        <div className="pb-4 text-left">{children}</div>
      </div>
    </div>
  );
}

export default Accordion;
