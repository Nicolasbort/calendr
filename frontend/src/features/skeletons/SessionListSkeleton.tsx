import SessionSkeleton from "components/skeletons/SessionSkeleton";

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
