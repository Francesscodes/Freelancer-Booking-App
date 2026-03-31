Freelancer Booking App
A lightweight, terminal-based application written in Python for managing and booking freelancers. 
The application uses a JSON-based storage system to persist freelancer data, including their availability, rates, and client reviews.

Features
View Freelancers: List all available professionals with their skills, hourly rates, and current status.

Booking System: Mark a freelancer as booked to update their availability in real-time.

Review System: Add and view text-based reviews for specific freelancers to track service quality.

Data Persistence: Automatically saves and loads data from a freelancers.json file to ensure information is kept between sessions.

Technical Stack
Language: Python 3.x

Data Format: JSON

Modules: json, os

Project Structure

main.py: The core logic containing the Freelancer and BookingApp classes.

freelancers.json: The database file storing the current state of all freelancers.

Default Freelancer List

The application initializes with the following default roles if no save file is found:

Faith: Social Media Manager ($20/hr)

Bisi: AI Automation Consultant ($15/hr)

Douglas: Web Developer ($18/hr)

Amaka: Product Manager ($15/hr)

Richard: SEO Expert ($10/hr)

How It Works
The Freelancer Class
Handles individual data for each freelancer, including:

to_dict(): Serializes object data for JSON storage.

show(): Displays formatted name, skill, rate, and status.

add_review(): Appends new feedback to the freelancer's profile.

The BookingApp Class
Manages the application flow and file I/O:

load_data(): Checks for freelancers.json. If missing, it seeds the file with default values.

save_data(): Writes the current state of all freelancer objects back to the JSON file.

run(): The main loop providing the interactive CLI menu.


Getting Started


Ensure Python is installed:

Bash
python --version

Run the application:

Bash
python main.py
Usage:
Follow the on-screen menu to (1) Show Freelancers, (2) Book, (3) Review, (4) View Reviews, or (5) Exit.

 Example JSON Structure
The data is stored in the following format:

JSON
[
  {
    "name": "Faith",
    "skill": "Social Media Manager",
    "rate": 20,
    "booked": true,
    "reviews": ["excellent services"]
  }
]
