import EditIcon from "/src/assets/Icons/edit-icon.svg?react";
import SearchIcon from "/src/assets/Icons/search-icon.svg?react";
import MessageIcon from "/src/assets/Icons/message-icon.svg?react";
import SettingsIcon from "/src/assets/Icons/settings-icon.svg?react";
import NotificationIcon from "/src/assets/Icons/notifications-icon.svg?react";

function Header() {
  return (
    <header id="hdr">
      <div className="hdr-cntnr">
        <button>
          <EditIcon className="svg" fill="rgb(19, 20, 21)" />
        </button>
        <div className="hdr-src-br">
          <SearchIcon className="svg" fill="rgb(138, 141, 145)" />
          <input type="text" placeholder="Search" />
        </div>
      </div>
      <div className="hdr-cntnr">
        <button>
          <MessageIcon className="svg" fill="rgb(156, 157, 158)" />
        </button>
        <button>
          <SettingsIcon className="svg" fill="rgb(156, 157, 158)" />
        </button>
        <button>
          <NotificationIcon className="svg" fill="rgb(156, 157, 158)" />
        </button>
        <button className="hdr-prfl-icn">
          <img src="src/assets/YoungImages/young_1.jpg" alt="" />
        </button>
      </div>
    </header>
  );
}

export default Header;
