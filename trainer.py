import subprocess
import time

# Define the file paths for odds.py, main.py, and the combining script
odds_script = "odds.py"
main_script = "main.py"
combine_script = "test.py"

# Define the time interval to wait between running main.py and the combining script (5 minutes)
interval = 360  # seconds

while True:
    # Run odds.py
    subprocess.run(["python", odds_script])

    # Wait for 5 minutes
    print(f"Waiting for {interval / 60} minutes...")
    time.sleep(interval)

    # Run main.py
    subprocess.run(["python", main_script])

    # Run the combining script
    subprocess.run(["python", combine_script])

    # Repeat the process
