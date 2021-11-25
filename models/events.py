from models.event import Event

event_1 = Event("30/11/2021", "CodeClan Party", 15, "Glasgow", "Party hard")
event_2 = Event("25/12/2021", "Christmas Party", 20, "Edinburgh", "Unbox presents")

events = [event_1, event_2]

def add_new_event(event):
    events.append(event)