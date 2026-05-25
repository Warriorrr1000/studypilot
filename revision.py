from api import get_response
from utils import save,load

def generate_quick_notes(text: str) -> str:
    """Generates quick concise notes on certain topic, or related to certain question."""
    text = text.strip()
    if not text:
        raise ValueError("\'text\' is a required argument.")
    response = get_response(prompt=text,instruction="Generate quick concise notes on the following topic/question.")
    entry = {
        "type" : "Quick Notes",
        "text" : text,
        "notes" : response
    }
    save(entry,"revision.json")
    return response

def extract_key_points(text: str) -> str:
    text = text.strip()
    if not text:
        raise ValueError("\'text\' is a required argument.")
    response = get_response(prompt=text,instruction="Extract Bullet-point Key points from this set of texts on a certain topic")
    entry = {
        "type" : "Key Points",
        "text" : text,
        "key_points" : response
    }
    save(entry,"revision.json")
    return response

def generate_revision_questions(content: str) -> str:
    content = content.strip()
    if not content:
        raise ValueError("\'content\' is a required argument.")
    response = get_response(prompt=content,instruction="Generate practice/revision questions from the following texts or topic.")
    entry = {
        "type" : "Revision Questions",
        "content" : content,
        "questions" : response
    }
    save(entry,"revision.json")
    return response

def view_revision_history(filter_type: str | None = None) -> str:
    data = load("revision.json")
    if not data:
        return "No history found."
    valid_filters = ["Quick Notes","Key Points","Revision Questions"]
    if filter_type is not None:
        filter_type = filter_type.strip()
        if filter_type not in valid_filters:
            raise ValueError(f"\'{filter_type}\' is not a valid filter.\n Valid Filters: {valid_filters}")
    output_msg = ["\n========== REVISION HISTORY ==========\n"]
    i = 1
    for item in data:
        if filter_type:
            if item['type'] != filter_type:
                continue
        output_msg.append(f"\n{i}. Type: {item['type']}\n")
        for key,value in item.items():
            if key == "type":
                continue
            formatted_key = key.replace("_"," ").title()
            output_msg.append(f"{formatted_key}: {value}\n")
        output_msg.append("\n---------------------------------\n")
        i += 1

    return "".join(output_msg)