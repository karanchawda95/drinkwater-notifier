import time, os
from plyer import notification

if __name__ == "__main__":
    icon_dir = os.path.dirname(os.path.abspath(__file__))
    notification.notify(
        title="***** Drink Water Now *****",
        message="\n--------------------------------",
        app_icon=os.path.join(icon_dir, "icon.ico"),
        timeout=10
    )
