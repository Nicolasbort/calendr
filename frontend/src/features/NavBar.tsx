import CalendrLogo from "calendr.png";
import { FiBell } from "react-icons/fi";

function NavBar() {
  return (
    <nav className="bg-white border-gray-200">
      <div className="max-w-screen-xl flex items-center justify-around xl:justify-between mx-auto py-4">
        <a
          href="https://calendr.com"
          className="flex items-center space-x-3 rtl:space-x-reverse"
        >
          <img src={CalendrLogo} className="h-8" alt="Calendr Logo" />
        </a>
        <ul className="font-medium flex flex-col p-0 border border-gray-100 rounded-lg bg-gray-50 rtl:space-x-reverse mt-0 border-0 bg-white">
          <li>
            <a
              href="#"
              className="block py-2 px-3 text-black bg-transparent rounded p-0 hover:opacity-75"
            >
              <FiBell />
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default NavBar;
