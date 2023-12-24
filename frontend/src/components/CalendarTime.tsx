interface Props {
  time: string;
  disabled?: boolean;
}

function CalendarTime({ time, disabled = false }: Props) {
  if (disabled) {
    return (
      <div className="p-3 text-gray-400 line-through rounded font-semibold border border-gray-300">
        {time}
      </div>
    );
  }

  return (
    <div className="p-3 bg-blue-200 text-blue-600 rounded font-semibold">
      {time}
    </div>
  );
}

export default CalendarTime;
