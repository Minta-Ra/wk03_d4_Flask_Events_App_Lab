from flask import render_template, request, redirect
from app import app
from models.events import events, add_new_event, delete_event
from models.event import Event
import datetime


# RENDER ALL SAVED EVENTS
@app.route("/events")
def index():
    return render_template("index.html", title="Events", events=events)


# ADD A NEW EVENT
@app.route("/events", methods=["POST"])
def add_event():
    # Date
    event_date = request.form["date"]
    split_date = event_date.split("-")
    event_date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    # Create a new task
    event_name = request.form["name_of_event"]
    event_num_of_guests = int(request.form["number_of_guests"])
    event_room_location = request.form["room_location"]
    event_description = request.form["description"]
    # Recurring
    event_recurring = False
    if "recurring" in request.form.keys():
        event_recurring = True
    newEvent = Event(event_date, event_name, event_num_of_guests, event_room_location, event_description, event_recurring)
    # Add task to the list
    add_new_event(newEvent)
    # Render the list
    return redirect("/events")


# DELETE AN EVENT
@app.route("/events/delete/<name>", methods=["POST"])
def delete(name):
    delete_event(name)
    return redirect("/events")