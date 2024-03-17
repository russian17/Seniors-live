import { event } from "../types/EventCard_type";

interface EventCardProps {
  event: event;
}

function EventCard({ event }: EventCardProps) {
  console.log(event.imageUrl);

  const date = {
    month: event.date.split("/")[0],
    day: event.date.split("/")[1],
    day_of_week: event.date.split("/")[2],
    time: event.date.split("/")[3],
  };

  const visible_atendees = event.atendees.slice(0, 3);
  const hidden_atendees =
    event.atendees.length > 3 ? event.atendees.length - 3 : 0;

  return (
    <div className="evnt-crd">
      <div
        className="evnt-img"
        style={{ backgroundImage: `url(${event.imageUrl})` }}
      >
        <div className="evnt-dt">
          <p>{event.date.split("/")[0].toLocaleUpperCase()}</p>
          <h3>{date.day.length === 1 ? "0" + date.day : date.day}</h3>
        </div>
        <div className="evnt-prsn-dscrptn">
          <h6>
            Profession
            <span>{event.proffesion}</span>
          </h6>
          <h6>
            Experience
            <span>{event.experience.toString()} years</span>
          </h6>
          <h6>
            Last worked
            <span>{event.last_worked}</span>
          </h6>
        </div>
      </div>
      <div className="evnt-dtls">
        <h6>
          {date.day_of_week} {date.time}
        </h6>
        <h5>
          {event.name} {event.surname}
        </h5>
        <p>
          {event.competences.slice(0, -1).map((competence) => (
            <>
              <span>{competence}</span>
              <span>&bull;</span>
            </>
          ))}
          {event.competences[event.competences.length - 1]}
        </p>
      </div>
      <div className="evnt-atnds">
        <div>
          {visible_atendees.map((atendee) => (
            <img
              src={atendee.photoUrl}
              alt={atendee.name + " " + atendee.surname}
            />
          ))}
          {hidden_atendees > 0 && <div className="evnt-hdn-atnds">+{hidden_atendees}</div>}
        </div>
        <button>Attend</button>
      </div>
    </div>
  );
}

export default EventCard;
