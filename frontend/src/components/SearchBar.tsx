import { searchTextAtom } from "atom";
import { useAtom } from "jotai";
import { memo, useEffect, useRef } from "react";
import { IoIosSearch } from "react-icons/io";

interface Props {
  placeholder?: string;
  searchDelay?: number;
  onSearch: (search: string) => void;
}

function SearchBar({ placeholder, searchDelay = 800, onSearch }: Props) {
  const [searchText, setSearchText] = useAtom(searchTextAtom);
  const firstMount = useRef(true);

  useEffect(() => {
    if (firstMount.current) {
      firstMount.current = false;
      return;
    }

    const delayDebounceFn = setTimeout(() => {
      onSearch(searchText);
    }, searchDelay);

    return () => clearTimeout(delayDebounceFn);
  }, [searchText]);

  return (
    <div className="relative max-w-[200px] sm:max-w-full">
      <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
        <IoIosSearch className="w-5 h-5 text-gray-500" />
      </div>
      <input
        type="search"
        className="block w-full px-4 py-2 ps-10 text-sm text-gray-900 border border-gray-300 outline-none rounded-full focus:ring-blue-500 focus:border-blue-500"
        value={searchText}
        onChange={({ target }) => setSearchText(target.value)}
        placeholder={placeholder}
      />
    </div>
  );
}

export default memo(SearchBar);
