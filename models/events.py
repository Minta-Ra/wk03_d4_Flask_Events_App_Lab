from models.event import Event
import datetime

event_1 = Event(datetime.date(2021, 11, 20), "CodeClan Party", 15, "Glasgow", "Party hard", True)
event_2 = Event(datetime.date(2021, 12, 25), "Christmas Party", 20, "Edinburgh", "Unbox presents", False)
event_3 = Event(datetime.date(2021, 11, 24), "Flask Lab", 20, "Zoom, VS Code", "Pair programming", True)
event_4 = Event(datetime.date(2021, 11, 26), "Flask HM", 1, "VS Code", "Weekend homework", False)
event_5 = Event(datetime.date(2022, 3, 11), "G28 Graduation", 20, "Zoom", "Graduation event", False)

events = [event_1, event_2, event_3, event_4, event_5]


def add_new_event(event):
    events.append(event)


def delete_event(event_name):
    event_to_delete = None
    for event in events:
        if event.name_of_event == event_name:
            event_to_delete = event
            break

    events.remove(event_to_delete)