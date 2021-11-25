from models.event import Event

event_1 = Event("30/11/2021", "CodeClan Party", 15, "Glasgow", "Party hard", True)
event_2 = Event("25/12/2021", "Christmas Party", 20, "Edinburgh", "Unbox presents", False)
event_3 = Event("25/11/2021", "Flask Lab", 20, "Zoom, VS Code", "Pair programming", True)
event_4 = Event("26/11/2021", "Flask HM", 1, "VS Code", "Weekend homework", False)
event_5 = Event("11/03/2023", "G28 Graduation", 20, "Zoom", "Graduation event", False)

events = [event_1, event_2, event_3, event_4, event_5]

def add_new_event(event):
    events.append(event)