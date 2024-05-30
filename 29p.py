class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add(self, other_time):
        total_seconds = self.seconds + other_time.seconds
        total_minutes = self.minutes + other_time.minutes + total_seconds // 60
        total_hours = self.hours + other_time.hours + total_minutes // 60

        new_seconds = total_seconds % 60
        new_minutes = total_minutes % 60
        new_hours = total_hours % 24  
        return Time(new_hours, new_minutes, new_seconds)

def main():
    try:
        # Create first time object
        time1 = Time(2, 45, 50)
        print(f"Time 1: {time1.display()}")
    except Exception as e:
        print(f"An error occurred while processing Time 1: {e}")

    try:
        # Create second time object
        time2 = Time(1, 20, 30)
        print(f"Time 2: {time2.display()}")
    except Exception as e:
        print(f"An error occurred while processing Time 2: {e}")

    try:
        # Add the two time objects
        time3 = time1.add(time2)
        print(f"Sum of Time 1 and Time 2: {time3.display()}")
    except Exception as e:
        print(f"An error occurred while adding Time 1 and Time 2: {e}")

if __name__ == "__main__":
    main()
