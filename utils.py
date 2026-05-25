import json

def format_duration(seconds: int) -> str:
    #seconds = duration in total seconds.
    try:
        seconds = int(seconds)
    except (ValueError,TypeError):
        raise ValueError(f"Duration must be a numeric value in seconds.")
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    formatted_time = f"{f'{hours}h ' if hours != 0 else ''}{f'{minutes}m ' if minutes != 0 else ''}{f'{secs}s ' if secs != 0 else ''}"
    return formatted_time

def average(values: list[int]) -> float:
    mean = sum(values) / len(values)
    return mean

def save(content: dict,file_path: str) -> None:
    if not content:
        raise ValueError("\'content\' is a required argument.")
    file_path = file_path.strip()
    if not file_path:
        raise ValueError("\'file_path\' is a required argument.")
    #Loading existing data.
    try:
        with open(f"data/{file_path}") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append(content)
    #Updating the data.
    try:
        with open(f"data/{file_path}","w") as f:
            json.dump(data,f,indent=4)
    except:
        raise Exception("An error occurred. Please try again.")
    
def load(file_path: str) -> list[dict]:
    file_path = file_path.strip()
    if not file_path:
        raise ValueError("\'file_path\' is a required argument.")
    #Loading data.
    try:
        with open(f"data/{file_path}") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        with open(f"data/{file_path}","w") as f:
            json.dump(data,f)
    return data