import SessionSkeleton from "features/skeletons/SessionSkeleton";

function SessionListSkeleton() {
  return (
    <>
      {[0, 1, 2, 3].map((index) => (
        <SessionSkeleton key={index} />
      ))}
    </>
  );
}

export default SessionListSkeleton;
