import classNames from "classnames";

function SessionSkeleton() {
  const sessionClassNames = classNames(
    "relative rounded-lg border py-3 px-6 animate-pulse"
  );
  const leftColorClassNames = classNames(
    "absolute left-0 top-0 bottom-0 rounded-tl-lg rounded-bl-lg w-[8px]"
  );

  return (
    <div className={sessionClassNames}>
      <div className={leftColorClassNames}></div>
      <div className="grid grid-cols-2">
        <div className="flex flex-col justify-start gap-4 text-left">
          <div className="h-4 bg-gray-300 rounded-full w-32"></div>
          <div className="h-4 bg-gray-300 rounded-full w-32"></div>
        </div>
        <div className="flex items-center justify-end">
          <div className="h-4  bg-gray-300 rounded-full w-24"></div>
        </div>
      </div>
    </div>
  );
}

export default SessionSkeleton;
