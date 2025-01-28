import psutil

def get_status():
    """
    اطلاعات مربوط به مصرف CPU و حافظه سیستم را بازمی‌گرداند.
    """
    # دریافت مصرف CPU به درصد
    cpu_usage = psutil.cpu_percent(interval=1)

    # دریافت اطلاعات حافظه
    memory_info = psutil.virtual_memory()
    memory_total = memory_info.total  # کل حافظه
    memory_used = memory_info.used    # حافظه استفاده‌شده
    memory_percent = memory_info.percent  # درصد استفاده

    # بازگرداندن داده‌ها به صورت دیکشنری
    return {
        "cpu_usage": cpu_usage,
        "memory": {
            "total": memory_total,
            "used": memory_used,
            "percent": memory_percent
        }
    }
