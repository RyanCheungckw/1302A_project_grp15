import json
from icalendar import Calendar

def parse_ics_schedule(file_path):
    """Parses an exported .ics schedule file into structured time slots."""
    with open(file_path, "rb") as f:
        cal = Calendar.from_ical(f.read())
    
    busy_slots = []
    for component in cal.walk():
        if component.name == "VEVENT":
            summary = component.get('summary')
            dtstart = component.get('dtstart').dt
            dtend = component.get('dtend').dt
            
            busy_slots.append({
                "title": summary,
                "day": dtstart.strftime("%a"),  # e.g., "Mon", "Tue"
                "start": dtstart.strftime("%H:%M"),
                "end": dtend.strftime("%H:%M")
            })
    return busy_slots
