import React from "react";

interface Props {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

function Modal({ children, isOpen, onClose }: Props) {
  if (!isOpen) return <></>;

  return (
    <div
      className="absolute top-0 bottom-0 left-0 right-0 bg-gray-100 bg-opacity-75"
      onClick={onClose}
    >
      <div className="flex justify-center items-center h-full">
        <div className="rounded-lg shadow">{children}</div>
      </div>
    </div>
  );
}

export default Modal;
