import os
import platform

def restart_system():
    """
    سیستم را ری‌استارت می‌کند.
    """
    system_platform = platform.system()

    if system_platform == "Windows":
        # دستور ری‌استارت برای ویندوز
        os.system("shutdown /r /t 0")
    elif system_platform in ["Linux", "Darwin"]:  # Darwin مربوط به macOS است
        # دستور ری‌استارت برای لینوکس و macOS
        os.system("sudo reboot")
    else:
        raise Exception("Unsupported platform")
