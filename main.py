from mail_to_sms import MailToSMS
import schedule, time


def text(message):
    print(f"sent message: {message}")
    MailToSMS(2165445367, "verizon wireless", "textbotethanf@gmail.com", "gxiqkxpieiloewav", message)

tasks = [
    # {
    #     "time": "",
    #     "message": "",
    # },
    {
        "time": "12:00",
        "message": "ankle stretches",
        "frequency": "day",
        "day": "day", # if you want it every day just type day
    },
    {
        "time": "13:00",
        "message": "take out the trash",
        "frequency": "day",
        "day": "monday", # if you want it every day just type day
    },
    {
        "time": "17:00",
        "message": "study linear",
        "frequency": "day",
        "day": "wednesday", # if you want it every day just type day
    },
    {
        "message": "do something on the 30",
        "frequency": "hour",
        "minute": "30"
    }
]

days = {
    "monday": schedule.every().monday,
    "tuesday": schedule.every().tuesday,
    "wednesday": schedule.every().wednesday,
    "thursday": schedule.every().thursday,
    "friday": schedule.every().friday,
    "saturday": schedule.every().saturday,
    "sunday": schedule.every().sunday,
    "day": schedule.every().day,
}

def main():
    #text("bruh")
    # create a scheduled task for every item in tasks
    for task in tasks:
        if task["frequency"] == "day":
            days[task["day"]].at(task["time"]).do(text, message=task["message"])
        elif task["frequency"] == "hour":
            schedule.every().hour.at(f":{task['minute']}").do(text, message=task["message"])

    print(schedule.get_jobs())
    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()