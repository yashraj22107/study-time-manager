import datetime
import time
import json
import os

class StudyManager:
    def __init__(self):
        self.study_data = {}
        self.load_data()
    
    def load_data(self):
        if os.path.exists("study_data.json"):
            with open("study_data.json", "r") as file:
                self.study_data = json.load(file)
        else:
            self.study_data = {
                "subjects": {},
                "total_study_time": 0,
                "study_sessions": []
            }
    
    def save_data(self):
        with open("study_data.json", "w") as file:
            json.dump(self.study_data, file)
    
    def add_subject(self):
        subject_name = input("Enter subject name: ")
        goal_hours = float(input("Enter weekly goal hours: "))
        
        self.study_data["subjects"][subject_name] = {
            "goal_hours": goal_hours,
            "completed_hours": 0,
            "sessions": []
        }
        self.save_data()
        print(f"Added {subject_name} with {goal_hours} hours weekly goal")
    
    def start_study_session(self):
        if not self.study_data["subjects"]:
            print("No subjects added yet!")
            return
        
        print("\nYour subjects:")
        subjects = list(self.study_data["subjects"].keys())
        for i, subject in enumerate(subjects, 1):
            print(f"{i}. {subject}")
        
        try:
            choice = int(input("Choose subject number: ")) - 1
            selected_subject = subjects[choice]
        except:
            print("Invalid choice!")
            return
        
        print(f"Starting study session for {selected_subject}...")
        print("Press Enter when you finish studying")
        
        start_time = datetime.datetime.now()
        input()
        end_time = datetime.datetime.now()
        
        study_duration = (end_time - start_time).total_seconds() / 3600
        study_hours = round(study_duration, 2)
        
        self.study_data["subjects"][selected_subject]["completed_hours"] += study_hours
        self.study_data["total_study_time"] += study_hours
        
        session_info = {
            "subject": selected_subject,
            "date": start_time.strftime("%Y-%m-%d %H:%M"),
            "duration": study_hours
        }
        self.study_data["study_sessions"].append(session_info)
        
        self.save_data()
        print(f"Great! You studied {study_hours} hours of {selected_subject}")
    
    def show_progress(self):
        print("\n=== STUDY PROGRESS ===")
        print(f"Total study time: {self.study_data['total_study_time']} hours")
        
        for subject, data in self.study_data["subjects"].items():
            completed = data["completed_hours"]
            goal = data["goal_hours"]
            progress = (completed / goal) * 100 if goal > 0 else 0
            remaining = max(0, goal - completed)
            
            print(f"\n{subject}:")
            print(f"  Completed: {completed} hours")
            print(f"  Goal: {goal} hours")
            print(f"  Progress: {progress:.1f}%")
            print(f"  Remaining: {remaining} hours")
    
    def show_recent_sessions(self):
        print("\n=== RECENT STUDY SESSIONS ===")
        sessions = self.study_data["study_sessions"][-5:]
        
        if not sessions:
            print("No study sessions recorded yet!")
            return
        
        for session in reversed(sessions):
            print(f"{session['date']} - {session['subject']}: {session['duration']} hours")
    
    def set_study_reminder(self):
        study_time = input("Enter study reminder time (HH:MM): ")
        message = input("Enter reminder message: ")
        
        try:
            reminder_time = datetime.datetime.strptime(study_time, "%H:%M").time()
            current_time = datetime.datetime.now().time()
            
            if reminder_time > current_time:
                print(f"Reminder set for {study_time}: {message}")
            else:
                print("Reminder set for tomorrow")
        except:
            print("Invalid time format! Use HH:MM")

def main():
    manager = StudyManager()
    
    while True:
        print("\n=== STUDY TIME MANAGER ===")
        print("1. Add Subject")
        print("2. Start Study Session")
        print("3. Show Progress")
        print("4. Recent Sessions")
        print("5. Set Reminder")
        print("6. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            manager.add_subject()
        elif choice == "2":
            manager.start_study_session()
        elif choice == "3":
            manager.show_progress()
        elif choice == "4":
            manager.show_recent_sessions()
        elif choice == "5":
            manager.set_study_reminder()
        elif choice == "6":
            print("Goodbye! Keep studying!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()