import EventCard from "./EventCard/EventCard";
import Header from "./Header/Header";
import "/src/styles/styles.scss";
import ChevronDown from "/src/assets/Icons/down-chevron.svg?react";
import { events } from "./HARDCODED/events";
import VerifiedIcon from "/src/assets/Icons/veified-icon.svg?react";
import { seniors } from "./HARDCODED/seniors";

function App() {
  return (
    <>
      <Header />
      <main id="main">
        <section className="lft-sctn">
          <div className="acc-inf">
            <img src="/src/assets/YoungImages/young_1.jpg" alt="" />
            <div>
              <h1>Jane Doe</h1>
              <VerifiedIcon className="svg" />
            </div>
            <span>@jane_doe</span>
          </div>
          <div className="acc-dtls">
            <h3>
              420 <span>Following</span>
            </h3>
            <h3>
              4.2k <span>Followers</span>
            </h3>
          </div>
          <div className="wh-fllw">
            <h3>Who to follow</h3>
            <div className="wh-fllw-accs">
              {seniors.map((senior) => (
                <div className="sgst-acc">
                  <div>
                    <img
                      src={senior.photoUrl}
                      alt={senior.name + " " + senior.surname}
                    />
                    <h4>
                      {senior.name} {senior.surname}
                      <span>
                        @
                        {senior.name.toLowerCase() +
                          "_" +
                          senior.surname.toLowerCase()}
                      </span>
                    </h4>
                  </div>
                  <button>Follow</button>
                </div>
              ))}
            </div>
            <span className="vw-mr">View more</span>
          </div>
        </section>
        <section className="evnt-sctn">
          <div className="evnt-sctn-top">
            <h2>Upcoming events</h2>
            <div>
              <p>
                Sort by: <span>Most recent</span>
              </p>
              <ChevronDown className="svg" fill="#fff" />
            </div>
          </div>
          <div className="evnt-sctn-evnts">
            {events.map((event) => (
              <EventCard event={event} />
            ))}
          </div>
        </section>
      </main>
    </>
  );
}

export default App;
