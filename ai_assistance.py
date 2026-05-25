from api import get_response
from utils import save,load

def ask_question(question: str) -> str:
    question = question.strip()
    if not question:
        raise ValueError(f"\'question\' is a required argument.")
    response = get_response(prompt=question, instruction="Answer clearly and briefly for a student.")
    entry = {
        "type" : "Q/A",
        "question" : question,
        "answer" : response
    }
    save(content=entry,file_path="history.json")
    return response
    
def summarize_text(text: str,word_limit: int = None) -> str:
    text = text.strip()
    if not text:
        raise ValueError(f"\'text\' is a required argument.")
    if word_limit:
        try:
            word_limit = int(word_limit)
        except (ValueError,TypeError):
            raise ValueError("\'word_limit\' must be an integer.")
    response = get_response(prompt=text,instruction=f"Summarize the following text into concise study notes.{f'[In {word_limit} to {word_limit + 5} words.]' if word_limit else ''}")
    entry = {
        "type" : "Summary",
        "text" : text,
        "summary" : response
    }
    save(content=entry,file_path="history.json")
    return response
    
def generate_quiz(topic: str,quiz_count: int = 5) -> str:
    topic = topic.strip()
    if not topic:
        raise ValueError(f"\'topic\' is a required argument.")
    if quiz_count:
        try:
            quiz_count = int(quiz_count)
        except (ValueError,TypeError):
            raise ValueError("\'quiz_count\' must be an integer.")
    quiz_questions = get_response(prompt=topic,instruction=f"Generate {quiz_count} quiz questions with answers.[Formatted Number-Wise]")
    entry = {
        "type" : "Quiz",
        "topic" : topic,
        "quizzes" : quiz_questions
    }
    save(entry,"history.json")
    return quiz_questions
    
def explain_topic(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        raise ValueError(f"\'topic\' is a required argument.")
    response = get_response(prompt=topic,instruction="Explain this topic in simple beginner-friendly language.")
    entry = {
        "type" : "Explanation",
        "topic" : topic,
        "explanation" : response
    }
    save(entry,"history.json")
    return response

def view_history(filter_type: str | None = None) -> str:
    data = load("history.json")
    if not data:
        return "No history found."
    valid_filters = ["Q/A","Summary","Quiz","Explanation"]
    if filter_type is not None:
        filter_type = filter_type.strip()
        if filter_type not in valid_filters:
            raise ValueError(f"\'{filter_type}\' is not a valid filter.\n Valid Filters: {valid_filters}")
    output_msg = ["\n========== HISTORY ==========\n"]
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
        output_msg.append("\n-------------------------\n")
        i += 1

    return "".join(output_msg)

                
    
        

