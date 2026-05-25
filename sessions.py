import json
from datetime import datetime

def load_session() -> list[dict]:
    try:
        with open("data/sessions.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        with open("data/sessions.json","w") as f:
            json.dump(data,f)
    return data

def start_session(subject: str) -> str:
    data = load_session()
    subject = subject.strip()
    if not subject:
        raise ValueError("\'subject\' is a required argument.")
    current_time = datetime.now().isoformat() #Str format for storing.
    for item in data:
        if item["active"]:
            # I was thinking to make a custom error for this situation here ,Lol
            #But for this small scale project i guess, that wasn't much necessary so i didn't make it.
            return "Cannot create another session, until the previous session is terminated."
    new_session = {
        "subject" : subject,
        "start_time" : current_time,
        "end_time" : None,
        "duration" : None,
        "active" : True
        }
    data.append(new_session)
    with open("data/sessions.json","w") as f:
        json.dump(data,f,indent=4)
    return "Session started successfully."    

def end_session() -> str:
    data = load_session()
    if not data:
        return "No study sessions found."
    current_time = datetime.now().isoformat() #Str format for storing
    for item in data:
        if item["active"]:
            start_time = datetime.fromisoformat(item["start_time"]) #Converting str to datetime obj.
            item["end_time"] = current_time #Storing str format
            current_time = datetime.fromisoformat(current_time) #Converting str -> datetime obj for calculations
            duration = current_time - start_time
            item["duration"] = duration.total_seconds()
            item["active"] = False
            with open("data/sessions.json","w") as f:
                json.dump(data,f,indent=4)
            return "Session ended successfully."
    return "No active study sessions found."

def view_sessions() -> str:
    data = load_session()
    if not data:
        return "No study sessions found."
    i = 1
    output_msg = [
        "\n========== SESSIONS ==========\n",
    ]
    for item in data:
        status = "Active" if item["active"] else "Ended"
        msg_lines = [f"\n{i}. Subject: {item['subject']}",f"\n   Start Time: {datetime.fromisoformat(item['start_time']).strftime('%d %b %Y, %I:%M %p')}"]
        if item['end_time']:
            msg_lines.append(f"\n   End Time: {datetime.fromisoformat(item['end_time']).strftime('%d %b %Y, %I:%M %p')}")
        if item['duration']:
            seconds = int(item['duration'])
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            secs = seconds % 60
            formatted_duration = f"{f'{hours}h ' if hours != 0 else ''}{f'{minutes}m ' if minutes != 0 else ''}{f'{secs}s ' if secs != 0 else ''}"
            msg_lines.append(f"\n   Duration: {formatted_duration}")
        msg_lines.append(f"\n   Status: {status}\n")
        msg_lines.append("\n-------------------------------- \n")

        for lines in msg_lines:
            output_msg.append(lines)
        i += 1
    return "".join(output_msg)

#Future functionality delete_session, it deletes the entire session history(only if session has ended.)
#get_active_session - returns all active sessions.
