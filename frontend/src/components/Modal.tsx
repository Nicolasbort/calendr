import { Dialog } from "@headlessui/react";
import React from "react";

interface Props {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

function Modal({ children, isOpen, onClose }: Props) {
  return (
    <Dialog className="relative z-50" open={isOpen} onClose={onClose}>
      <div className="fixed inset-0 bg-black/30" aria-hidden="true" />
      <div className="fixed inset-0 flex w-screen items-center justify-center p-4">
        <Dialog.Panel className="w-full max-w-sm mx-auto rounded-lg shadow-lg bg-white py-5">
          {children}
        </Dialog.Panel>
      </div>
    </Dialog>
  );
}

export default Modal;
