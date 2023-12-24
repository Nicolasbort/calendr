function PatientSkeleton() {
  return (
    <div className="relative rounded-lg border px-3 py-4 bg-white animate-pulse">
      <div className="flex justify-between items-center text-left">
        <div className="h-3 bg-gray-300 rounded-full w-32"></div>
        <div className="h-3 bg-gray-300 rounded-full w-24"></div>
      </div>
    </div>
  );
}

export default PatientSkeleton;
