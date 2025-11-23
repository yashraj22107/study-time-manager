# Study Time Manager

A simple Python application to help students manage their study time effectively.

## What It Does

This program helps you track your study hours for different subjects and monitor your progress towards weekly study goals.

## Features

- Add subjects with weekly study goals
- Track study sessions with automatic timing
- View progress for each subject
- See recent study sessions
- Set study reminders
- Automatic data saving

## How to Use

1. Run the program
2. Choose from these options:

### 1. Add Subject
- Enter subject name (like "Mathematics", "Physics")
- Set weekly study goal in hours

### 2. Start Study Session
- Select a subject from your list
- Press Enter to start studying
- Press Enter again when finished
- Program automatically calculates study time

### 3. Show Progress
- See total study time
- View progress for each subject
- Check how much time remains to reach goals

### 4. Recent Sessions
- View last 5 study sessions
- See date, subject, and duration

### 5. Set Reminder
- Set study time reminders
- Add custom reminder messages

### 6. Exit
- Save all data and close program

## Data Storage

All your study data is automatically saved in `study_data.json` file. Don't delete this file or you'll lose your progress.

## Requirements

- Python 3.x
- No additional packages needed

## How to Run

```bash
python study_manager.py
