# import time 
import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Eat Breakfast",
        message="Improved Energy Levels: Breakfast provides the body with the essential nutrients and energy needed to kick-start the day. After an overnight fast, eating breakfast replenishes glycogen stores and stabilizes blood sugar levels, preventing fatigue.",
        # app_icon= r"E:\\New folder\\bf.png",  # Use raw string (r) or double backslashes
        # app_icon = "B-icon.png",
        # app_icon  =  "E:\New folder", 
        timeout   =  2
    )
