import psutil

def get_processes():
    """
    تعداد پردازه‌های در حال اجرا روی سیستم را بازمی‌گرداند.
    """
    # دریافت لیست پردازه‌ها
    processes = psutil.pids()
    # بازگرداندن تعداد پردازه‌ها
    return {
        "total_processes": len(processes)
    }
