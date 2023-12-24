import PatientSkeleton from "features/skeletons/PatientSkeleton";

function PatientListSkeleton() {
  return (
    <>
      {[0, 1, 2, 3].map((index) => (
        <PatientSkeleton key={index} />
      ))}
    </>
  );
}

export default PatientListSkeleton;
