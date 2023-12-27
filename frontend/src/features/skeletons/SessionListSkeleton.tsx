import SessionSkeleton from "features/skeletons/SessionSkeleton";

function SessionListSkeleton() {
  return (
    <div className="py-5 flex flex-col gap-3">
      {[0, 1, 2, 3].map((index) => (
        <SessionSkeleton key={index} />
      ))}
    </div>
  );
}

export default SessionListSkeleton;
