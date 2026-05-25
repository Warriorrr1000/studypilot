from api import get_response
from utils import save,load
import json

def generate_flashcards(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        raise ValueError("\'topic\' is a required argument.")
    flashcard = get_response(prompt=topic,instruction="Generate flashcards in Question and Answer format.")
    data = {
        "topic": topic,
        "flashcard": flashcard
    }
    save(data,"flashcards.json")
    return flashcard

def view_flashcards() -> str:
    data = load("flashcards.json")
    if not data:
        return "No flashcards found."
    i = 1
    output_msg = [
        "\n========== Flashcards ==========\n"
    ]
    for item in data:
        msg_lines = [f"{i}. {item['topic']}","\nFlashcard:\n",f"{item['flashcard']}\n","\n-------------------------\n"]
        for lines in msg_lines:
            output_msg.append(lines)
        i += 1
    return "".join(output_msg)

def delete_flashcards(flashcard_no: int) -> str:
    data = load("flashcards.json")
    if not data:
        return "No flashcards found."
    if not flashcard_no:
        raise ValueError("\'flashcard_no\' is a required argument.")
    try:
        flashcard_no = int(flashcard_no)
        selection = data[flashcard_no-1]['topic']
    except (ValueError,TypeError,IndexError):
        raise ValueError(f"\'{flashcard_no}\' is not a valid flashcard number.")
    data.pop(flashcard_no-1)
    with open("data/flashcards.json","w") as f:
        json.dump(data,f,indent=4)
    return "Flashcard deleted successfully."

