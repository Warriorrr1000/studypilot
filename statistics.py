from sessions import load_session
from utils import format_duration,average

def get_total_study_time() -> str:
    data = load_session()
    if not data:
        return "No study session data found."
    total_study_time_sec = 0
    for item in data:
        if item['duration']:
            total_study_time_sec += int(item['duration'])
    return format_duration(total_study_time_sec)

def total_sessions_count() -> int:
    data = load_session()
    return len(data)

def get_session_status() -> str:
    data = load_session()
    if not data:
        return "No study sessions data found."
    active = 0
    ended = 0
    for item in data:
        if item['active']:
            active += 1
        else:
            ended += 1
    return f"Active sessions: {active}\nEnded sessions: {ended}"

def get_average_session_time() -> str:
    data = load_session()
    if not data:
        return "No study session data found."
    session_durations = []
    for item in data:
        if item['duration']:
            session_durations.append(int(item['duration']))
    average_time = average(session_durations)
    return format_duration(average_time)

def get_longest_session() -> str:
    data = load_session()
    if not data:
        return "No study session data found."
    sessions = {}
    for item in data:
        if item['duration']:
            sessions[f"{item['subject']}"] = int(item['duration'])
    if not sessions:
        return "No completed study sessions found."
    longest_session = max(sessions.items(),key=lambda item: item[1])
    return f"Longest Session:\nSubject: {longest_session[0]}\nDuration: {format_duration(longest_session[1])}"

def get_subject_wise_study_time() -> str:
    data = load_session()
    if not data:
        return "No study session data found."
    session = {}
    for item in data:
        if item["duration"]:
            if not item['subject'] in session:
                session[f'{item["subject"]}'] = int(item['duration'])
            else:
                session[f'{item["subject"]}'] += int(item['duration'])
    output = []
    for subject,duration in session.items():
        output.append(f"{subject} : {format_duration(duration)}\n")
    return "".join(output)

#Later on if i continue this project beside for Cs50P then i'll add:
"""
get_most_studied_subject()
get_today_study_time()
get_weekly_study_time() etc"""

    
