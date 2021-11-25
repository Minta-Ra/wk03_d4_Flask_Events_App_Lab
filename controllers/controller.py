from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Events", events=events)


@app.route('/events', methods=["POST"])
def add_event():
    # return render_template()

    # Create a new task
    event_name = request.form["name_of_event"]
    event_date = request.form["date"]
    event_num_of_guests = int(request.form["number_of_guests"])
    event_room_location = request.form["room_location"]
    event_description = request.form["description"]
    newEvent = Event(event_date, event_name, event_num_of_guests, event_room_location, event_description)
    # Add task to the list
    add_new_event(newEvent)
    # Render the list
    return index()