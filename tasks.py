import time
import json

def add_task(task: str,deadline: str = None) -> str:
    task = task.strip()
    current_time = time.ctime()
    if not task:
        raise ValueError("\'task\' is a required argument.")
    new_data = {
        "task" : task,
        "added_on" : current_time,
        "deadline" : deadline,
        "done" : False
    }
    
    try:
        with open("data/tasks.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append(new_data)
    
    try:
        with open("data/tasks.json","w") as f:
            json.dump(data,f,indent=4)
    except:
        raise Exception("An Error Occurred. please try again.")
    
    return f"Task:{task} added successfully"

def load_task() -> list[dict]:
    try:
        with open("data/tasks.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        with open("data/tasks.json","w") as f:
            json.dump(data,f)
    return data
        
def view_task() -> str:
    data = load_task()
    if not data:
        return "No tasks found."
    i = 1
    output_msg = [
        "\n========== TASKS ==========",
    ]
    for item in data:
        status = "Completed" if item['done'] == True else "Pending"
        msg = f"""\n
{i}. {item["task"]}
     Status: {status}
     Added On: {item["added_on"]}
     {f"Deadline: {item['deadline']}" if item['deadline'] != None else ""}
     
-------------------------------- \n
        """
        output_msg.append(msg)
        i += 1
    return "".join(output_msg)
    
def mark_completed(task_no: int) -> str:
    data = load_task()
    if not data:
        return "No tasks found."
    if not task_no:
        raise ValueError("\'task_no\' is a required argument.")
    try:
        selection = data[task_no-1]['done']
    except IndexError:
        raise ValueError(f"{task_no} is not a valid task number")
    if selection:
        return "Task already completed."
    else:
        data[task_no-1]['done'] = True
        with open("data/tasks.json","w") as f:
            json.dump(data,f,indent=4)
        return "Task marked as completed."
    
def delete_task(task_no: int) -> str:
    data = load_task()
    if not data:
        return "No tasks found."
    if not task_no:
        raise ValueError("\'task_no\' is a required argument.")
    try:
        selection = data[task_no-1]['task']
    except IndexError:
        raise ValueError(f"{task_no} is not a valid task number")
    data.pop(task_no-1)
    with open("data/tasks.json","w") as f:
            json.dump(data,f,indent=4)
    return "Task deleted successfully."
    
def edit_task(task_no: int,new_task: str) -> str:
    data = load_task()
    new_task = new_task.strip()
    if not data:
        return "No tasks found."
    if not task_no:
        raise ValueError("\'task_no\' is a required argument.")
    if not new_task:
        raise ValueError("\'new_task\' is a required argument.")
    try:
        previous_task = data[task_no-1]['task']
    except IndexError:
        raise ValueError(f"{task_no} is not a valid task number")
    data[task_no-1]['task'] = new_task
    with open("data/tasks.json","w") as f:
        json.dump(data,f,indent=4)
    return f"Task edited successfully.\nPrevious Task: {previous_task}\nCurrent Task: {new_task}"

