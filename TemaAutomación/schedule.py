import schedule
import time

def job():
    print("Job running...")

# Schedule the job every 10 seconds
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
