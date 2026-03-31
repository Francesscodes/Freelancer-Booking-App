import json
import os

DATA_FILE = "freelancers.json"

DEFAULT_FREELANCERS = [
    {"name": "Faith",   "skill": "Social Media Manager",      "rate": 20, "booked": False, "reviews": []},
    {"name": "Bisi",    "skill": "AI Automation Consultant",   "rate": 15, "booked": False, "reviews": []},
    {"name": "Douglas", "skill": "Web Developer",              "rate": 18, "booked": False, "reviews": []},
    {"name": "Amaka",   "skill": "Product Manager",            "rate": 15, "booked": False, "reviews": []},
    {"name": "Richard", "skill": "SEO Expert",                 "rate": 10, "booked": False, "reviews": []},
]


class Freelancer:

    def __init__(self, name, skill, rate, booked=False, reviews=None):
        self.name = name
        self.skill = skill
        self.rate = rate
        self.booked = booked
        self.reviews = reviews if reviews is not None else []

    def to_dict(self):
        return {
            "name": self.name,
            "skill": self.skill,
            "rate": self.rate,
            "booked": self.booked,
            "reviews": self.reviews,
        }

    def show(self):
        status = "Booked" if self.booked else "Available"
        print(f"{self.name} | {self.skill} | ${self.rate}/hr | {status}")

    def add_review(self, review):
        self.reviews.append(review)

    def show_reviews(self):
        if not self.reviews:
            print("No reviews yet")
        else:
            print(f"Reviews for {self.name}:")
            for r in self.reviews:
                print(f"  - {r}")


class BookingApp:

    def __init__(self):
        self.freelancers = []

    

    def load_data(self):
        """Load from JSON file; seed with defaults if the file doesn't exist."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                records = json.load(f)
            self.freelancers = [Freelancer(**r) for r in records]
            print(f"Loaded {len(self.freelancers)} freelancers from {DATA_FILE}.")
        else:
            self.freelancers = [Freelancer(**r) for r in DEFAULT_FREELANCERS]
            self.save_data()          # create the file on first run
            print("No save file found — loaded default freelancers.")

    def save_data(self):
        """Serialize all freelancers to JSON."""
        with open(DATA_FILE, "w") as f:
            json.dump([f.to_dict() for f in self.freelancers], f, indent=2)

 
    def show_freelancers(self):
        print("\nFreelancers:")
        for i, f in enumerate(self.freelancers):
            print(f"  {i+1}. ", end="")
            f.show()

    def book_freelancer(self, index):
        if 0 <= index < len(self.freelancers):
            f = self.freelancers[index]
            if f.booked:
                print("Already booked!")
            else:
                f.booked = True
                self.save_data()
                print(f"{f.name} has been booked.")
        else:
            print("Invalid selection.")

    def add_review(self, index, review):
        if 0 <= index < len(self.freelancers):
            self.freelancers[index].add_review(review)
            self.save_data()
            print("Review added successfully!")
        else:
            print("Invalid freelancer.")

    def show_reviews(self, index):
        if 0 <= index < len(self.freelancers):
            self.freelancers[index].show_reviews()
        else:
            print("Invalid freelancer.")

   
    def run(self):
        self.load_data()
        while True:
            print("\n=== Freelancer Booking App ===")
            print("1. Show Freelancers")
            print("2. Book a Freelancer")
            print("3. Add a Review")
            print("4. View Reviews")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_freelancers()
            elif choice == '2':
                self.show_freelancers()
                try:
                    idx = int(input("Enter freelancer number to book: ")) - 1
                    self.book_freelancer(idx)
                except ValueError:
                    print("Enter a valid number.")
            elif choice == '3':
                self.show_freelancers()
                try:
                    idx = int(input("Enter freelancer number to review: ")) - 1
                    review = input("Enter your review: ")
                    self.add_review(idx, review)
                except ValueError:
                    print("Enter a valid number.")
            elif choice == '4':
                self.show_freelancers()
                try:
                    idx = int(input("Enter freelancer number to view reviews: ")) - 1
                    self.show_reviews(idx)
                except ValueError:
                    print("Enter a valid number.")
            elif choice == '5':
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = BookingApp()
    app.run()