import psutil

def get_processes():
    
    processes = psutil.pids()
    return {
        "total_processes": len(processes)
    }
