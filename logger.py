from datetime import datetime


def log_run(status):

    with open("automation_log.txt", "a") as log_file:

        log_file.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {status}\n"
        )