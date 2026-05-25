#Importing Custom made functions(or modules) by me using aliases.
import ai_assistance as ai
import flashcards as fc
import revision as rv
import sessions as session
import statistics as stats
import tasks as tk

#Other modules.
import os
import time
from colorama import Fore, Style, init
init()

#I have separated every functional part in different files, this file will more likely be menu.

def main() -> None:
    show_intro()
    while True:
        show_main_menu()
        user_choice = validate_menu_choice(7)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                ai_assistance_menu()
            case 2:
                clear_screen()
                revision_menu()
            case 3:
                clear_screen()
                flashcards_menu()
            case 4:
                clear_screen()
                session_menu()
            case 5:
                clear_screen()
                task_menu()
            case 6:
                clear_screen()
                stats_menu()
            case _:
                exit_menu("Thanks for using StudyPilot.!")
                break

def ai_assistance_menu() -> None:
    while True:
        txt = [
            "\n========== AI ASSISTANCE ==========\n",
            "\n1. Ask Question\n",
            "2. Summarize Text\n",
            "3. Generate Quiz\n",
            "4. Explanation of Topic\n",
            "5. View History\n",
            "6. Exit"
            ]
        print("".join(txt))
        user_choice = validate_menu_choice(6)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                print("\n========== ASK AI ==========\n")
                try:
                    response = ai.ask_question(input("Enter your question: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nAnswer:\n{response}")
                back()
            case 2:
                clear_screen()
                print("\n========== TEXT SUMMARIZER ==========\n")
                text = input("Enter your text to summarize: ")
                word_limit = input("Enter a approximate word limit of the summary[press enter to skip]: ")
                try:
                    response = ai.summarize_text(text=text,word_limit=word_limit)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nSummary:\n{response}")
                back() 
            case 3:
                clear_screen()
                print("\n========== QUIZ GENERATOR ==========\n")
                topic = input("Enter the topic of quiz: ")
                quiz_count = input("Number of questions[press enter to skip]: ")
                if not quiz_count.strip():
                    quiz_count = 5
                try:
                    response = ai.generate_quiz(topic=topic,quiz_count=quiz_count)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nQuestions:\n{response}")
                back()      
            case 4:
                clear_screen()
                print("\n========== TOPIC EXPLANATION ==========\n")
                try:
                    response = ai.explain_topic(input("Enter a topic: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nExplanation:\n{response}")
                back()
            case 5:
                clear_screen()
                filter_type = input("Enter a filter to see specific history type [press enter to see all]: ")
                if not filter_type.strip():
                    filter_type = None
                try:
                    response = ai.view_history(filter_type=filter_type)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case _:
                exit_menu()
                break
            
def revision_menu() -> None:
    while True:
        txt = [
            "\n========== REVISION TOOLS ==========\n",
            "\n1. Generate Quick Notes\n",
            "2. Extract Key Points\n",
            "3. Generate Revision Questions\n",
            "4. View History\n",
            "5. Exit"
        ]
        print(''.join(txt))
        user_choice = validate_menu_choice(5)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                print("\n========== QUICK NOTES GENERATOR ==========\n")
                try:
                    response = rv.generate_quick_notes(input("Enter a topic or text: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nQuick Notes:\n{response}")
                back()
            case 2:
                clear_screen()
                print("\n========== KEY POINT EXTRACTOR ==========\n")
                try:
                    response = rv.extract_key_points(input("Enter your text: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nKey Points:\n{response}")
                back()
            case 3:
                clear_screen()
                print("\n========== REVISION QUESTIONS ==========\n")
                try:
                    response = rv.generate_revision_questions(input("Enter a topic or text: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nRevision Questions:\n{response}")
                back()
            case 4:
                clear_screen()
                filter_type = input("Enter a filter to see specific history type [press enter to see all]: ")
                if not filter_type.strip():
                    filter_type = None
                try:
                    response = rv.view_revision_history(filter_type=filter_type)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case _:
                exit_menu()
                break
            
def flashcards_menu() -> None:
    while True:
        txt = [
            "\n========== FLASHCARDS ==========\n",
            "\n1. Generate Flashcards\n",
            "2. View Flashcards\n",
            "3. Delete Flashcard\n",
            "4. Exit"
        ]
        print(''.join(txt))
        user_choice = validate_menu_choice(4)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                print("\n========== GENERATE FLASHCARDS ==========\n")
                try:
                    response = fc.generate_flashcards(input("Enter a topic: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"\nGenerated Flashcards:\n{response}")
                back()
            case 2:
                clear_screen()
                print(fc.view_flashcards())
                back()
            case 3:
                clear_screen()
                print("\n========== DELETE FLASHCARD ==========\n")
                flashcard = fc.view_flashcards()
                print(flashcard)
                if flashcard == "No flashcards found.":
                    back()
                    continue
                try:
                    response = fc.delete_flashcards(input("Enter a flashcard number to delete: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case _:
                exit_menu()
                break
            
def session_menu() -> None:
    while True:
        txt = [
            "\n========== STUDY SESSION TRACKER ==========\n",
            "\n1. Start Study Session\n",
            "2. End Study Session\n",
            "3. View Session History\n",
            "4. Exit"
        ]
        print(''.join(txt))
        user_choice = validate_menu_choice(4)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                print("\n========== START STUDY SESSION ==========\n")
                try:
                    response = session.start_session(input("Enter subject: "))
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 2:
                clear_screen()
                print("\n========== END STUDY SESSION ==========\n")
                try:
                    response = session.end_session()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 3:
                clear_screen()
                try:
                    response = session.view_sessions()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case _:
                exit_menu()
                break
        
def task_menu() -> None:
    while True:
        txt = [
            "\n========== TASK MANAGER ==========\n",
            "\n1. Add Task\n",
            "2. View Tasks\n",
            "3. Mark Task as Completed\n",
            "4. Edit Task\n",
            "5. Delete Task\n",
            "6. Exit"
        ]
        print(''.join(txt))
        user_choice = validate_menu_choice(6)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                print("\n========== ADD TASK ==========\n")
                task = input("Enter task title: ")
                deadline = input("Enter deadline [press enter to skip]: ").strip()
                if not deadline:
                    deadline = None
                try:
                    response = tk.add_task(task=task,deadline=deadline)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 2:
                clear_screen()
                try:
                    response = tk.view_task()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 3:
                clear_screen()
                print("\n========== COMPLETE TASK ==========\n")
                tasks = tk.view_task()
                print(tasks)
                if tasks == "No tasks found.":
                    back()
                    continue
                try:
                    task_no = is_valid_int(input("Enter task number to mark as completed: "),"Task number cannot be negative or zero.")
                    response = tk.mark_completed(task_no=task_no)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 4:
                clear_screen()
                print("\n========== EDIT TASK ==========\n")
                tasks = tk.view_task()
                print(tasks)
                if tasks == "No tasks found.":
                    back()
                    continue
                try:
                    task_no = is_valid_int(input("Enter task number to edit: "),"Task number cannot be negative or zero.")
                    new_task = input("Enter updated task: ")
                    response = tk.edit_task(task_no=task_no,new_task=new_task)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 5:
                clear_screen()
                print("\n========== DELETE TASK ==========\n")
                tasks = tk.view_task()
                print(tasks)
                if tasks == "No tasks found.":
                    back()
                    continue
                try:
                    task_no = is_valid_int(input("Enter a task number to delete it: "),"Task number cannot be negative or zero.")
                    response = tk.delete_task(task_no=task_no)
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case _:
                exit_menu()
                break

def stats_menu() -> None:
    while True:
        txt = [
            "\n========== STUDY STATISTICS ==========\n",
            "\n1. View Total Study Time\n",
            "2. View Total Sessions Count\n",
            "3. View Session Status\n",
            "4. View Average Session Duration\n",
            "5. View Longest Study Session\n",
            "6. View Subject-wise Study Time\n",
            "7. Exit"
        ]
        print(''.join(txt))
        user_choice = validate_menu_choice(7)
        if user_choice is None:
            continue
        
        match user_choice:
            case 1:
                clear_screen()
                print("\n========== TOTAL STUDY TIME ==========\n")
                try:
                    response = stats.get_total_study_time()
                except Exception as e:
                    error(e)
                    back()
                    continue
                if response != "No study session data found.":
                    print(f"Total study time: {response}")
                else:
                    print(response)
                back()
            case 2:
                clear_screen()
                print("\n========== TOTAL SESSIONS ==========\n")
                try:
                    response = stats.total_sessions_count()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(f"Total Sessions: {response}")
                back()
            case 3:
                clear_screen()
                print("\n========== SESSION STATUS ==========\n")
                try:
                    response = stats.get_session_status()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 4:
                clear_screen()
                print("\n========== AVERAGE SESSION DURATION ==========\n")
                try:
                    response = stats.get_average_session_time()
                except Exception as e:
                    error(e)
                    back()
                    continue
                if response != "No study session data found.":
                    print(f"Average Duration: {response}")
                else:
                    print(response)
                back()
            case 5:
                clear_screen()
                print("\n========== LONGEST STUDY SESSION ==========\n")
                try:
                    response = stats.get_longest_session()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case 6:
                clear_screen()
                print("\n========== SUBJECT-WISE STUDY TIME ==========\n")
                try:
                    response = stats.get_subject_wise_study_time()
                except Exception as e:
                    error(e)
                    back()
                    continue
                print(response)
                back()
            case _:
                exit_menu()
                break
            
def show_intro() -> None:
    clear_screen()
    txt = [
        "\n========== StudyPilot ==========\n",
        "\nWelcome to StudyPilot!\n",
        "\nA terminal(CLI)-based study environment with A.I Integration.",
        "\nFeatures:\n",
        "- AI Assistance\n",
        "- Revision Tools\n",
        "- Flashcards\n",
        "- Study Session Tracking\n",
        "- Task Management System\n",
        "- Study Statistics\n",
        "\nStudyPilot - It is created by Warrior🜲.\nIt was created as the final project of CS50 - Introduction to programming with python.\nIt is an upgraded version of my previous project which i did when i was taking CS50. \nProject Link: https://github.com/Warriorrr1000/ai-study-companion\n",
       "\nNote: More updates may come in the future as I continue improving this project beyond CS50.\n"     
    ]
    print(''.join(txt))
    back()

def show_main_menu() -> None:
    txt = [
        "\n========== MAIN MENU ==========\n",

        "\n1. AI Assistance\n",
        "2. Revision Tools\n",
        "3. Flashcards\n",
        "4. Study Session Tracker\n",
        "5. Task Manager\n",
        "6. Study Statistics\n",
        "7. Exit\n"
    ]
    print(''.join(txt))
    
def clear_screen() -> None:
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    
def error(message: Exception) -> None:
    if not message:
        raise ValueError("\'message\' is a required argument.")
    print(Fore.RED + f"\nError({type(message).__name__}): {message}" + Style.RESET_ALL)
    
def back() -> None:
    input(Fore.CYAN + "\nPress Enter to continue..." + Style.RESET_ALL)
    clear_screen()
    
def exit_menu(msg: str = None) -> None:
    if msg is None:
        msg = "Returning to main menu..."
    print(Fore.YELLOW + f"\n{msg}" + Style.RESET_ALL)
    time.sleep(1)
    clear_screen()
    
def validate_menu_choice(total_options: int) -> int | None:
    #This part is for the developer for using this function correctly.
    try:
        if not total_options:
            raise ValueError("\'total_options\' is a required argument.")
        total_options = int(total_options)
        if total_options <= 0:
            raise ValueError("The menu choices cannot be negative or zero.")
    except Exception as e:
        error(e)
        back()
        return None
    #Taking input from user (handling users input and all in short.)
    try:
        user_input = int(input("Choose an option: "))
        if user_input not in range(1,total_options+1):
            raise ValueError
        return user_input
    except ValueError:
        error("Invalid Input. Please enter a valid menu choice.")
        time.sleep(1)
        back()
        return None
    
def is_valid_int(number: int,custom_error: str = None) -> int:
    """This function only accepts Positive Integer.
    On entering Negative int or zero it raises error."""
    #Especially designed for my functions usecases.
    if custom_error is None:
        custom_error = "The number cannot be negative or zero."
    custom_error = custom_error.strip()
    if not custom_error:
        raise ValueError("\'custom_error\' cannot be empty.")
    try:
        number = int(number)
        if number <= 0:
            raise ValueError(custom_error)
        return number
    except ValueError as e:
        raise ValueError(e)
          
if __name__=="__main__":
    main()


    