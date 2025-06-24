import time

def log_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")